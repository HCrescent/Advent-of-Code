"""Day 15 Advent_of_Code 2021"""
# heuristic: horizontal + vertical cells to objective (because we cannot move diagonally it must take H+V moves)


class MinHeap:
	# min priority queue
	def __init__(self, size):
		self.heap = [None for _ in range(size)]
		self.last_i = 0  # points to the end of the list (for adding new elements)

	def insert(self, element):
		""" Inserts an element at the bottom of our "virtual" tree, and then bubbles the value up accordingly

		:param element: Any comparable type data
		"""
		try:
			self.heap[self.last_i] = element  # insert new element at last index
		except IndexError:
			print("Index Error, needed more heap space.")
			raise SystemExit(1)
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
		self.last_i -= 1  # move back one to the last element in the list
		tmp_hold = self.heap[0]  # temporarily hold the value until we return it
		self.heap[0] = None  # replace that spot with our empty value
		# swap root and last nodes
		self.heap[self.last_i], self.heap[0] = self.heap[0], self.heap[self.last_i]
		curr_i = 0  # set our current index to node 0
		# Run until match case: no children or compared child fails
		while True:
			# at the start of each iteration update the children node pointers
			child_l = curr_i * 2 + 1  # set new index of left child
			child_r = curr_i * 2 + 2  # set new index of right child
			# build our case expression
			try:
				children = f"{0 if self.heap[child_l] is None else 1}{0 if self.heap[child_r] is None else 1}"
			except IndexError:
				children = "00"
			match children:
				case "11":  # both children nodes exist
					if self.heap[child_l] <= self.heap[child_r]:
						compared_child = child_l
					else:
						compared_child = child_r
				case "10":  # right child is None, left child exists
					compared_child = child_l
				case "01":  # left child is None, right child exists
					compared_child = child_r
				case _:  # both children are None
					break
			# if the current node is greater than the compared child, swap them and update current node
			if self.heap[curr_i] > self.heap[compared_child]:
				self.heap[curr_i], self.heap[compared_child] = self.heap[compared_child], self.heap[curr_i]
				curr_i = compared_child
			else:  # current node is in its correct spot we are done
				break
		return tmp_hold  # return our popped value

	def printHeap(self):
		print([_ for _ in self.heap[:self.last_i]])


class AStarNode:
	# things we need on init, weight of cell, its x and y position
	def __init__(self, coord):
		self.parent = None
		self.coordinate = coord
		self.data = data[coord[0]][coord[1]]  # in our problem we want to sum the weights of the paths
		# distance from start + weight of cell
		self.G = abs(start_position[0] - coord[0]) + abs(start_position[1] - coord[1]) + data[coord[0]][coord[1]]
		# distance from end (exact)
		self.H = abs(end_position[0] - coord[0]) + abs(end_position[1] - coord[1])
		self.F = self.G + self.H

	def __eq__(self, other):
		return self.F == other.F

	def __lt__(self, other):
		return self.F < other.F

	def __le__(self, other):
		return self.F <= other.F

	def __repr__(self):
		return f"coord: {self.coordinate}, G: {self.G}, H: {self.H}, F:{self.F}"

	def __hash__(self):  # we want to identify unique nodes by their position in the grid
		return hash(self.coordinate)


with open("input/day15.txt", 'r') as infile:
	data = [[int(char) for char in line.rstrip()] for line in infile]
UNIQUE_PATH_LEFT = {}
UNIQUE_PATH = {}
WIDTH = len(data)
print("width:", WIDTH)


def display_graphXY(graph):
	"""Displays matrix in proper X, Y orientation for human viewing.

	:param graph: list of lists - a matrix
	:return:
	"""
	for i in range(len(graph[0]))[::-1]:
		flipped_list = [graph[_][i] for _ in range(len(graph))]
		print(flipped_list)
	return


def display_graph(graph):
	for _ in graph:
		print(_)


# noinspection PyUnresolvedReferences
def aStarTraverse(graph, start, end):
	length = len(graph)
	width = len(graph[0])
	open_nodes = MinHeap(length*width)  # maximum heap size number grid spaces
	open_nodes.insert(AStarNode(start))
	closed_nodes = set()
	neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
	while True:
		current_node = open_nodes.pop()  # pop current node from priority queue
		closed_nodes.add(current_node)  # add it to the closed set
		for each in neighbors:
			new_coordinate = (current_node.coordinate[0] + each[0], current_node.coordinate[1] + each[1])
			if new_coordinate[0] > -1 and new_coordinate[1] > -1:
				try:
					graph[new_coordinate[0]][new_coordinate[1]]
				except IndexError:
					print(new_coordinate, "OUT OF RANGE BITCH")
				if new_coordinate not in closed_nodes:
					open_nodes.insert(AStarNode(new_coordinate))  # add node to open nodes
	pass


if __name__ == "__main__":
	start_position = (0, 0)
	end_position = (WIDTH-1, WIDTH-1)
	display_graphXY(data)
	aStarTraverse(data, start_position, end_position)
