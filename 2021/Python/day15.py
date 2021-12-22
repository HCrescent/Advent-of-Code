"""Day 15 Advent_of_Code 2021"""
# NOTES: path limit should be 20 spaces, possibly less, end points should be the diagonal cross section
with open("input/day15.txt", 'r') as infile:
	data = [list(map(int, line.rstrip())) for line in infile]
data[0][0] = 0
UNIQUE_PATH_LEFT = {}
UNIQUE_PATH_RIGHT = {}


def display_graph(graph):
	"""Displays matrix in proper X, Y orientation for human viewing.

	:param graph: list of lists - a matrix
	:return:
	"""
	for i in range(len(graph[0]))[::-1]:
		flipped_list = [graph[_][i] for _ in range(len(graph))]
		print(flipped_list)
	return


def west(matrix, x, y, record):
	# coord added together < width of matrix plus one and not a node
	return (x - 1) + y <= 9 and record.get(f"m:{x-1},{y}", 1)


def north(matrix, x, y, record):
	# north is < 9 and not a node
	return x + (y + 1) <= 9 and record.get(f"m:{x},{y+1}", 1)


def east(matrix, x, y, record):
	# east is < 9 and not a node
	return (x + 1) + y <= 9 and record.get(f"m:{x+1},{y}", 1)


def south(matrix, x, y, record):
	# south is below 9 and not a node
	return x + (y - 1) <= 9 and record.get(f"m:{x},{y-1}", 1)


def basin_mapper(matrix, x, y, record):
	"""RECURSION BABY, We start at our basin origin, record a key-string for our legal node and then step in to the
	next movement.

	:param matrix: list - list of lists matrix
	:param x: int - x coordinate in our matrix
	:param y: int - y coordinate in our matrix
	:param record: dict - dictionary of nodes : False for bool key checks while pathing
	:return: dict - the most up to date record of nodes
	"""
	print(f"we are at m:{x},{y}")
	if x + y == 9:
		print(f"we found endpoint {x},{y}")
		return record
	record[f"m:{x},{y}"] = False
	match x, y:
		case x, y if 0 < x < len(matrix)-1 and 0 < y < len(matrix[x])-1:  # case for matrix[x][y] has 4 neighbors.
			if south(matrix, x, y, record):
				record = basin_mapper(matrix, x, y-1, record)
			if north(matrix, x, y, record):
				record = basin_mapper(matrix, x, y+1, record)
			if east(matrix, x, y, record):
				record = basin_mapper(matrix, x+1, y, record)
			if west(matrix, x, y, record):
				record = basin_mapper(matrix, x-1, y, record)
		# top edge case, always 3 neighbors: south north east
		case x, y if x == 0 and 0 < y < len(matrix[x])-1:
			if south(matrix, x, y, record):
				record = basin_mapper(matrix, x, y-1, record)
			if north(matrix, x, y, record):
				record = basin_mapper(matrix, x, y+1, record)
			if east(matrix, x, y, record):
				record = basin_mapper(matrix, x+1, y, record)
		# right edge case, always 3 neighbors: south east west
		case x, y if 0 < x < len(matrix)-1 and y == len(matrix[x])-1:
			if south(matrix, x, y, record):
				record = basin_mapper(matrix, x, y-1, record)
			if east(matrix, x, y, record):
				record = basin_mapper(matrix, x+1, y, record)
			if west(matrix, x, y, record):
				record = basin_mapper(matrix, x-1, y, record)
		# bottom edge case, always 3 neighbors: south north west
		case x, y if x == len(matrix)-1 and 0 < y < len(matrix[x])-1:
			if south(matrix, x, y, record):
				record = basin_mapper(matrix, x, y-1, record)
			if north(matrix, x, y, record):
				record = basin_mapper(matrix, x, y+1, record)
			if west(matrix, x, y, record):
				record = basin_mapper(matrix, x-1, y, record)
		# left edge case, always 3 neighbors: north east west
		case x, y if 0 < x < len(matrix)-1 and y == 0:
			if north(matrix, x, y, record):
				record = basin_mapper(matrix, x, y+1, record)
			if east(matrix, x, y, record):
				record = basin_mapper(matrix, x+1, y, record)
			if west(matrix, x, y, record):
				record = basin_mapper(matrix, x-1, y, record)
		# top left corner case, always 2 neighbors: north east
		case x, y if x == 0 and y == 0:
			if north(matrix, x, y, record):
				record = basin_mapper(matrix, x, y+1, record)
			if east(matrix, x, y, record):
				record = basin_mapper(matrix, x+1, y, record)
		# top right corner case, always 2 neighbors: south east
		case x, y if x == 0 and y == len(matrix[x])-1:
			if south(matrix, x, y, record):
				record = basin_mapper(matrix, x, y-1, record)
			if east(matrix, x, y, record):
				record = basin_mapper(matrix, x+1, y, record)
		# bottom left corner case, always 2 neighbors: north west
		case x, y if x == len(matrix)-1 and y == 0:
			if north(matrix, x, y, record):
				record = basin_mapper(matrix, x, y+1, record)
			if west(matrix, x, y, record):
				record = basin_mapper(matrix, x-1, y, record)
		# bottom right corner case, always 2 neighbors: south west
		case x, y if x == len(matrix)-1 and y == len(matrix[x])-1:
			if south(matrix, x, y, record):
				record = basin_mapper(matrix, x, y-1, record)
			if west(matrix, x, y, record):
				record = basin_mapper(matrix, x-1, y, record)
	return record


def recursive_cave(connected_caves, path_taken='', part2=False, flag=False):
	name = list(CAVES.keys())[list(CAVES.values()).index(connected_caves)]  # name of cave we are in
	path_taken += f"{name},"
	if name == "end":
		UNIQUE_PATHS[path_taken] = True  # update new unique path
		return  # return up one level of recursion to find more paths
	for each in connected_caves:
		if each == "start":
			continue
		new_flag = flag
		if each.islower() and f"{each}," in path_taken:  # if each is a small cave and already in our path
			if part2 and not new_flag:
				new_flag = True
			else:
				continue
		recursive_cave(CAVES[each], path_taken, part2, new_flag)
	return  # this should be our return when theres no options to move


if __name__ == "__main__":
	display_graph(data)
	path_taken = {}
	path_taken = basin_mapper(data, 0, 0, path_taken)
	# for n in range(len(data[0])):
	# 	new = [data[_][n] for _ in range(len(data))]
	# 	print(new)
# print("part 1: ")
# print("part 2: ")
