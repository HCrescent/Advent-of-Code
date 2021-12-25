"""Day 15 Advent_of_Code 2021"""
# NOTES: path limit should be 20 spaces, possibly less, end points should be the diagonal cross section
with open("input/day15.txt", 'r') as infile:
	data = [list(map(int, line.rstrip())) for line in infile]
data[0][0] = 0
UNIQUE_PATH_LEFT = {}
UNIQUE_PATH = {}
WIDTH = len(data)
print(WIDTH)


def display_graph(graph):
	"""Displays matrix in proper X, Y orientation for human viewing.

	:param graph: list of lists - a matrix
	:return:
	"""
	for i in range(len(graph[0]))[::-1]:
		flipped_list = [graph[_][i] for _ in range(len(graph))]
		print(flipped_list)
	return


def west(x, y, path_taken):
	# coord added together < width of matrix plus one and not a node
	return x+y != WIDTH and (f"({x-1},{y})," not in path_taken)


def north(x, y, path_taken):
	# north is < 9 and not a node
	return x+y != WIDTH and (f"({x},{y+1})," not in path_taken)


def east(x, y, path_taken):
	# east is < 9 and not a node
	return x + y != WIDTH and (f"({x+1},{y})," not in path_taken)


def south(x, y, path_taken):
	# south is below 9 and not a node
	return x + y != WIDTH and (f"({x},{y-1})," not in path_taken)


def recursive_move_right(matrix, risk, x, y, path_taken=''):
	risk += matrix[x][y]
	# print(f"we are at m:{x},{y}", risk)
	if x + y == WIDTH:
		# print(f"we found endpoint {x},{y}", risk)
		if UNIQUE_PATH.get(f"({x},{y})", 9999999) > risk:
			UNIQUE_PATH[f"({x},{y})"] = risk  # update new unique path
			print(len(UNIQUE_PATH))
		return  # return up one level of recursion to find more paths
	if path_taken.count("),") > WIDTH:
		return
	path_taken += f"({x},{y}),"
	match x, y:
		case x, y if 0 < x < len(matrix)-1 and 0 < y < len(matrix[x])-1:  # case for matrix[x][y] has 4 neighbors.
			if south(x, y, path_taken):
				recursive_move(matrix, risk, x, y-1, path_taken)
			if north(x, y, path_taken):
				recursive_move(matrix, risk, x, y+1, path_taken)
			if east(x, y, path_taken):
				recursive_move(matrix, risk, x+1, y, path_taken)
			if west(x, y, path_taken):
				recursive_move(matrix, risk, x-1, y, path_taken)
		# top edge case, always 3 neighbors: south north east
		case x, y if x == 0 and 0 < y < len(matrix[x])-1:
			if south(x, y, path_taken):
				recursive_move(matrix, risk, x, y-1, path_taken)
			if north(x, y, path_taken):
				recursive_move(matrix, risk, x, y+1, path_taken)
			if east(x, y, path_taken):
				recursive_move(matrix, risk, x+1, y, path_taken)
		# right edge case, always 3 neighbors: south east west
		case x, y if 0 < x < len(matrix)-1 and y == len(matrix[x])-1:
			if south(x, y, path_taken):
				recursive_move(matrix, risk, x, y-1, path_taken)
			if east(x, y, path_taken):
				recursive_move(matrix, risk, x+1, y, path_taken)
			if west(x, y, path_taken):
				recursive_move(matrix, risk, x-1, y, path_taken)
		# bottom edge case, always 3 neighbors: south north west
		case x, y if x == len(matrix)-1 and 0 < y < len(matrix[x])-1:
			if south(x, y, path_taken):
				recursive_move(matrix, risk, x, y-1, path_taken)
			if north(x, y, path_taken):
				recursive_move(matrix, risk, x, y+1, path_taken)
			if west(x, y, path_taken):
				recursive_move(matrix, risk, x-1, y, path_taken)
		# left edge case, always 3 neighbors: north east west
		case x, y if 0 < x < len(matrix)-1 and y == 0:
			if north(x, y, path_taken):
				recursive_move(matrix, risk, x, y+1, path_taken)
			if east(x, y, path_taken):
				recursive_move(matrix, risk, x+1, y, path_taken)
			if west(x, y, path_taken):
				recursive_move(matrix, risk, x-1, y, path_taken)
		# top left corner case, always 2 neighbors: north east
		case x, y if x == 0 and y == 0:
			if north(x, y, path_taken):
				recursive_move(matrix, risk, x, y+1, path_taken)
			if east(x, y, path_taken):
				recursive_move(matrix, risk, x+1, y, path_taken)
		# top right corner case, always 2 neighbors: south east
		case x, y if x == 0 and y == len(matrix[x])-1:
			if south(x, y, path_taken):
				recursive_move(matrix, risk, x, y-1, path_taken)
			if east(x, y, path_taken):
				recursive_move(matrix, risk, x+1, y, path_taken)
		# bottom left corner case, always 2 neighbors: north west
		case x, y if x == len(matrix) - 1 and y == 0:
			if north(x, y, path_taken):
				recursive_move(matrix, risk, x, y+1, path_taken)
			if west(x, y, path_taken):
				recursive_move(matrix, risk, x-1, y, path_taken)
		# bottom right corner case, always 2 neighbors: south west
		case x, y if x == len(matrix)-1 and y == len(matrix[x])-1:
			if south(x, y, path_taken):
				recursive_move(matrix, risk, x, y-1, path_taken)
			if west(x, y, path_taken):
				recursive_move(matrix, risk, x-1, y, path_taken)
	return  # this should be our return when theres no options to move


def balance(path_dict, x=0, y=WIDTH-1):
	while x < WIDTH:
		path_dict[f"({x},{y})"] -= data[x][y]
		x += 1
		y -= 1
	return path_dict


if __name__ == "__main__":
	display_graph(data)
	recursive_move(data, 0, 0, 0)
	print(UNIQUE_PATH)
	UNIQUE_PATH_LEFT = balance(UNIQUE_PATH.copy())
	UNIQUE_PATH.clear()
	print(UNIQUE_PATH)
	print(UNIQUE_PATH_LEFT)
	recursive_move(data, 0, WIDTH - 1, WIDTH - 1)
	print(UNIQUE_PATH)
	for each in UNIQUE_PATH:
		totals = [UNIQUE_PATH[each] + UNIQUE_PATH_LEFT[each] for each in UNIQUE_PATH]
	totals.sort()
	print("part 1: ", totals[0])
# print("part 2: ")
