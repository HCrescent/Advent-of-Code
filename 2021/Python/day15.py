"""Day 15 Advent_of_Code 2021"""
# heuristic: horizontal + vertical cells to objective (because we cannot move diagonally it must take H+V moves)
with open("input/day15.txt", 'r') as infile:
	data = [[int(char) for char in line.rstrip()] for line in infile]  # two dimensional list/matrix grid


class MinHeap:
	# min priority queue
	def __init__(self):
		self.heap = []
		self.last_i = 0  # points to the end of the list (for adding new elements)

	def insert(self, element):
		""" Inserts an element at the bottom of our "virtual" tree, and then bubbles the value up accordingly

		:param element: Any comparable type data
		"""
		self.heap.append(element)  # insert new element at last index
		parent_i = (self.last_i-1) // 2  # set index of parent node
		curr_i = self.last_i  # we want the swap index to be our current elements placement
		self.last_i += 1  # increase index for the last element
		while parent_i > -1:  # while we are not at the root (if the parent is -1 current is at i = 0)
			# if the parent node is larger than the current node
			if self.heap[parent_i] > self.heap[curr_i]:
				# swap the two nodes
				self.heap[parent_i], self.heap[curr_i] = self.heap[curr_i], self.heap[parent_i]
				# now the parent index becomes the current index
				curr_i = parent_i
				# calculate the index of the new parent node of our current node
				parent_i = (parent_i-1) // 2
			else:  # the parent node is larger than current node, we are done swapping things around
				break

	def pop(self):
		""" removes root node (element at position 0), adjusts the heap and returns the node/element

		:return: any type - heap should take any comparable element so whatever type is contained is being returned
		"""
		hold_min = self.heap.pop()  # pop the last element off the list (this wont be the min yet)
		tmp_hold = hold_min  # store that popped element for later
		self.last_i -= 1  # move back one to the last element in the list
		if self.heap:  # if the heap isn't empty
			self.heap[0], hold_min = hold_min, self.heap[0]  # swap the held item and the root node, we are holding min
			curr_i = 0  # set our current index to node 0
			l_child_i = 1  # set index of the first left child
			# while current index is less than the length of the list
			while l_child_i < self.last_i:
				r_child_i = l_child_i + 1  # right child always one position higher
				if r_child_i < self.last_i:  # if r_child_i exists in heap
					if self.heap[l_child_i] > self.heap[r_child_i]:  # if the left child is greater than the right child
						l_child_i = r_child_i  # now l_child_i is pointing to the smallest of either child
				self.heap[curr_i] = self.heap[l_child_i]
				curr_i = l_child_i  # update the current position pointer to the position of the child we moved
				l_child_i = 2 * curr_i + 1  # get new left child
			# the node we just inserted at current index might not be in the correct position
			# so now we have to follow its roots up
			while curr_i > 0:  # run till we hit the root
				parent_i = (curr_i - 1) // 2  # get position of parent of current position
				if tmp_hold < self.heap[parent_i]:  # if our held value is less than parent
					self.heap[curr_i] = self.heap[parent_i]  # current position becomes the parent value
					curr_i = parent_i  # current position updates to the now "empty" parent
				else:  # if held value is greater than parent we are done
					break
			self.heap[curr_i] = tmp_hold  # finally place the value in its rightful place
		return hold_min  # return our held value

	def printHeap(self):
		print([_ for _ in self.heap[:self.last_i]])


class AStarNode:
	# things we need on init, weight of cell, its x and y position
	def __init__(self, coord: tuple):
		"""

		:param coord: Tuple - (x, y) form of 2D list location
		"""
		self.parent = None  # need parent node in order to retrace the path
		self.coordinate = coord
		self.weight = data[coord[0]][coord[1]]  # in our problem we want to sum the weights of the paths
		self.G = None
		self.H = abs(end_position[0] - coord[0]) + abs(end_position[1] - coord[1])  # distance from end (exact)
		self.F = 0

	def tracePath(self):
		""" generates the path taken by recursively climbing the tree and bringing all the coordinates down

		:return: List - list of tuples which are the coordinates of the path taken
		"""
		if self.parent is None:
			return [self.coordinate]
		pathing = self.parent.tracePath()
		pathing = pathing + [self.coordinate]
		return pathing

	def connectNode(self, other):
		self.parent = other
		self.G = self.parent.G + self.weight
		self.F = self.G + self.H

	# these comparison operators are overwritten so we can store AStarNodes compared by F value in our heap
	def __eq__(self, other):
		return self.F == other.F

	def __lt__(self, other):
		return self.F < other.F

	def __le__(self, other):
		return self.F <= other.F

	def __repr__(self):
		return f"{self.coordinate}, G: {self.G}, H: {self.H}, F:{self.F}"

	def __hash__(self):  # we want to identify unique nodes in our closed set by their position in the grid
		return hash(self.coordinate)


def gridNodes(matrix):
	""" initializes all nodes for each spot in the matrix, so that they are all addressable by x, y

	:param matrix: List - 2D list of risk weights
	:return: List - 2D list of A* nodes
	"""
	new_grid = [row.copy() for row in matrix]
	for x, row in enumerate(new_grid):
		for y, _ in enumerate(row):
			new_grid[x][y] = AStarNode((x, y))
	return new_grid


def aStarTraverse(graph, start: tuple, end: tuple):
	start_node = graph[start[0]][start[1]]
	open_nodes = MinHeap()  # maximum heap size number grid spaces
	start_node.G = 0  # give our starting node a G of 0
	start_node.F = 0 + start_node.H  # give our starting node F value for heap sorting
	open_nodes.insert(start_node)  # insert starting node
	closed_nodes = set()
	movements = ((1, 0), (-1, 0), (0, 1), (0, -1))
	while open_nodes.last_i > 0:  # while open nodes isn't empty
		current_node = open_nodes.pop()  # pop current node from priority queue
		if current_node.coordinate == end:
			return current_node.G  # return path cost (current_node.tracedPath() if you want the actual path)
		closed_nodes.add(current_node.coordinate)  # add it to the closed set
		for each in movements:  # each possible movement from here
			# calculate the new position based on the movement tuple
			new_x, new_y = current_node.coordinate[0] + each[0], current_node.coordinate[1] + each[1]
			# due to python recognizing negative index as displacement from the end, i need to make these checks
			# because an index error wont raise on access, but for our case a negative number means were are
			# out of bounds of our graph matrix
			if new_x > -1 and new_y > -1:
				try:  # making sure a node can exist at this spot, by checking data existing in the graph
					neighbor_node = graph[new_x][new_y]  # assign a nicer reference
				except IndexError:  # the test resulted in index error out of graph bounds
					continue  # don't access and skip to next iteration
				if (new_x, new_y) not in closed_nodes:
					proposed_G = current_node.G + neighbor_node.weight  # proposed g cost after move
					if neighbor_node.G is None:  # nodes are initialized with None
						neighbor_node.connectNode(current_node)  # give the node a parent and calc G and F (H inside)
						open_nodes.insert(neighbor_node)  # add node to open nodes
					elif proposed_G <= neighbor_node.G:
						neighbor_node.connectNode(current_node)  # overwrite parent with better path and update values
						open_nodes.insert(neighbor_node)  # add node to open nodes
	return "Failed to find the end"


def expandData(matrix):
	""" expands input data set according to part 2 instructions

	:param matrix: List - 2D list
	:return: List - Expanded 2D list
	"""
	reference = matrix.copy()
	# we want to expand our data set by 5 times with modified values of the initial data
	for row in range(len(reference)):
		for cell in range(4):  # adding 4 more grids horizontally
			matrix[row] = matrix[row] + [(weight+cell) % 9 + 1 for weight in reference[row]]
	reference = matrix.copy()  # update reference copy
	for cell in range(4):  # add 4 more grids vertically
		for row in reference:
			matrix.append([(weight+cell) % 9 + 1 for weight in row])
	return matrix


if __name__ == "__main__":
	start_position = (0, 0)  # path start
	end_position = (len(data)-1, len(data[0])-1)  # path end the opposite corner of origin
	node_graph = gridNodes(data)
	path_cost = aStarTraverse(node_graph, start_position, end_position)
	print("part 1: ", path_cost)
	data = expandData(data)  # expand data set for part 2
	end_position = (len(data) - 1, len(data[0]) - 1)  # get new endpoint
	node_graph2 = gridNodes(data)
	path_cost = aStarTraverse(node_graph2, start_position, end_position)
	print("part 2: ", path_cost)
