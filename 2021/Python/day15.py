"""Day 15 Advent_of_Code 2021"""
# heuristic: horizontal + vertical cells to objective (because we cannot move diagonally it must take H+V moves)
from random import randint


class MinHeap:
	def __init__(self, size):
		self.heap = [None for _ in range(size)]
		self.last_i = 0  # points to the end of the list (for adding new elements)
		self.swap_i = 0  # index of current node
		self.parent_i = 0  # index of the parent node

	def insert(self, element):
		self.heap[self.last_i] = element  # insert new element at last index
		self.parent_i = self.last_i // 2  # set index of parent node
		self.swap_i = self.last_i  # we want the swap index to be our current elements placement
		self.last_i += 1  # increase index for the last element
		while self.parent_i > -1:  # while we are not at the root (if the parent is -1 we current is at i = 0)
			# if the parent node is larger than the current node
			if self.heap[self.parent_i] > self.heap[self.swap_i]:
				# swap the two nodes
				self.heap[self.parent_i], self.heap[self.swap_i] = self.heap[self.swap_i], self.heap[self.parent_i]
				# now the parent index becomes the current index
				self.swap_i = self.parent_i
				# calculate the index of the new parent node of our current node
				self.parent_i = self.parent_i // 2
			else:  # the parent node is larger than current node, we are done swapping things around
				break

	def remove(self, element):
		self.last_i -= 1

	def pop(self):
		self.last_i -= 1

	def printHeap(self):
		print([_ for _ in self.heap if _])


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


def aStarTraverse(graph, start, end):
	open_nodes = [AStarNode(start)]
	closed_nodes = []
	for each in open_nodes:
		print(each.F)
	pass


if __name__ == "__main__":
	start_position = (0, 0)
	end_position = (WIDTH-1, WIDTH-1)
	display_graphXY(data)
	aStarTraverse(data, start_position, end_position)
	origin = AStarNode((0, 1))
	one = AStarNode((1, 1))
	two = AStarNode((2, 0))
	print("part 1: ")
	print("origin: Coordinate:", origin.coordinate, "weight:", origin.data, "G:", origin.G, "H:", origin.H, "F:", origin.F)
	print("one: Coordinate:", one.coordinate, "weight:", one.data, "G:", one.G, "H:", one.H, "F:", one.F)
	print("two: Coordinate:", two.coordinate, "weight:", two.data, "G:", two.G, "H:", two.H, "F:", two.F)
	# print("part 2: ")
	test_heap = MinHeap(100_000)
	temp_list = [randint(1, 100) for _ in range(50)]
	temp_list.append(1)
	print(len(temp_list))
	for _ in temp_list:
		test_heap.insert(_)
	test_heap.printHeap()
