"""Day 12 Advent_of_Code 2022"""
# part 2 is bruteforce, and could be returned to and improved, maybe a rewrite
# based off my 2021 day 15 work on A*
import heapq
alpha = "abcdefghijklmnopqrstuvwxyz"
translate = {char: i+1 for i, char in enumerate(alpha)}
translate.update({"S": 1, "E": translate['z']})  # use 0 for start point and z's value for E
with open("input/day12.txt", 'r') as infile:
	data = [[char for char in line.rstrip()] for line in infile]  # two dimensional list/matrix grid
lowest_points = set()
for x in range(len(data)):
	for y in range(len(data[x])):
		if data[x][y] == 'S':
			start_position = (x, y)
			lowest_points.add(start_position)  # S for part 2 purposes is 'a' height
		if data[x][y] == "E":
			end_position = (x, y)
		if data[x][y] == 'a':  # for part 2 track all a's
			lowest_points.add((x, y))
data = [[translate[char] for char in line] for line in data]  # translate all values to integers


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
		self.G = self.parent.G + 1
		self.F = self.G + self.H

	# these comparison operators are overwritten so we can store AStarNodes compared by F value in our heap
	def __eq__(self, other):
		return self.F == other.F

	def __lt__(self, other):
		return self.F < other.F

	def __le__(self, other):
		return self.F <= other.F

	def __repr__(self):
		return f"{self.coordinate} G:{self.G} H:{self.H} F:{self.F}"

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


def MinNodes(matrix):  # grabs all 'a' node coordinates in the grid
	a_points = []
	point_H = []
	for x, row in enumerate(matrix):
		for y, _ in enumerate(row):
			if matrix[x][y].weight == 1:
				a_points.append(matrix[x][y].coordinate)
				point_H.append(matrix[x][y].H)
	return [each[1] for each in sorted(zip(point_H, a_points))]


def resetNodes(matrix):  # clear parents and F costs and G from the processed node grid
	for x, row in enumerate(matrix):
		for y, _ in enumerate(row):
			matrix[x][y].parent = None
			matrix[x][y].G = None
			matrix[x][y].F = 0
	return


def aStarTraverse(graph, start: tuple, end: tuple):
	start_node = graph[start[0]][start[1]]
	open_nodes = []
	start_node.G = 0  # give our starting node a G of 0
	start_node.F = 0 + start_node.H  # give our starting node F value for heap sorting
	heapq.heappush(open_nodes, start_node)  # insert starting node
	closed_nodes = set()
	movements = ((1, 0), (-1, 0), (0, 1), (0, -1))
	while open_nodes:  # while open nodes isn't empty
		current_node = heapq.heappop(open_nodes)  # pop current node from priority queue
		if current_node.coordinate == end:
			return len(current_node.tracePath())-1  # return path cost (current_node.tracedPath() if you want the actual path)
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
				if neighbor_node.weight > current_node.weight+1:  # if the step is too high
					continue  # skip node
				if (new_x, new_y) not in closed_nodes:
					proposed_G = current_node.G + 1  # proposed g cost after move
					if neighbor_node.G is None:  # nodes are initialized with None
						neighbor_node.connectNode(current_node)  # give the node a parent and calc G and F (H inside)
						heapq.heappush(open_nodes, neighbor_node)  # add node to open nodes
					elif proposed_G <= neighbor_node.G:
						neighbor_node.connectNode(current_node)  # overwrite parent with better path and update values
						heapq.heappush(open_nodes, neighbor_node)  # add node to open nodes
	return 1_000_000


if __name__ == "__main__":
	node_graph = gridNodes(data)
	# noinspection PyUnboundLocalVariable
	path_length = aStarTraverse(node_graph, start_position, end_position)
	print("part 1: ", path_length)
	resetNodes(node_graph)
	starting_choices = MinNodes(node_graph)
	part2_lengths = []
	for start in starting_choices:
		part2_lengths.append(aStarTraverse(node_graph, start, end_position))
		resetNodes(node_graph)
	print("part 2: ", min(part2_lengths))
