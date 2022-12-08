"""Day 08 Advent_of_Code 2022"""
with open("input/day08.txt", 'r') as infile:
	data = [[int(each) for each in line.rstrip()] for line in infile]


def treeVisible(coord):
	""" checks if tree at coordinate is visible from outside the grid

	:param coord: Tuple - (int, int) - coordinate
	:return: Bool - True if visible, False if not
	"""
	x, y = coord
	height = data[y][x]
	for sub_x in range(x):  # west direction
		if data[y][sub_x] >= height:
			break  # not visible from west
	else:  # didn't break: Tree visible from west
		return True
	for sub_x in range(x+1, len(data[y])):  # east direction
		if data[y][sub_x] >= height:
			break  # not visible from east
	else:  # didn't break: Tree visible from east
		return True
	for sub_y in range(y):  # north direction
		if data[sub_y][x] >= height:
			break  # not visible from north
	else:  # didn't break: Tree visible from north
		return True
	for sub_y in range(y+1, len(data)):  # south direction
		if data[sub_y][x] >= height:
			break  # not visible from south
	else:  # didn't break: Tree visible from south
		return True
	return False  # got here: tree is not visible


def visibleFromTree(coord):
	""" counts the number of trees visible from treehouse in each cardinal direction,
	the scenic score is the product of each cardinal count
	:param coord: Tuple - (int, int) - coordinate
	:return: Int - scenic score
	"""
	x, y = coord
	height = data[y][x]  # height of treehouse tree
	countN, countS, countE, countW = 0, 0, 0, 0
	for sub_x in range(x)[::-1]:  # west direction
		if data[y][sub_x] >= height:
			countW += 1
			break  # we cant see any more trees this direction
		else:
			countW += 1
	for sub_x in range(x+1, len(data[y])):  # east direction
		if data[y][sub_x] >= height:
			countE += 1
			break  # we cant see any more trees this direction
		else:
			countE += 1
	for sub_y in range(y)[::-1]:  # north direction
		if data[sub_y][x] >= height:
			countN += 1
			break  # we cant see any more trees this direction
		else:
			countN += 1
	for sub_y in range(y+1, len(data)):  # south direction
		if data[sub_y][x] >= height:
			countS += 1
			break  # we cant see any more trees this direction
		else:
			countS += 1
	return countN * countW * countE * countS


def part1():
	""" counts the number of trees in the grid that are visible from outside the edge

	:return: Int - number of visible trees
	"""
	visible_trees = 0
	y_edge = len(data)-1
	x_edge = len(data[0])-1
	for y in range(len(data)):
		for x in range(len(data[y])):
			if y == 0:  # all top trees are visible
				visible_trees += 1
				continue
			elif y == y_edge:  # all bottom trees are visible
				visible_trees += 1
				continue
			if x == 0:  # all left edge trees are visible
				visible_trees += 1
				continue
			elif x == x_edge:  # all right edge trees are visible
				visible_trees += 1
				continue
			if treeVisible((x, y)):  # if tree visible from any cardinal direction
				visible_trees += 1
	return visible_trees


def part2():
	""" get the maximum possible scenic score for any tree in the grid

	:return: Int - highest scenic score
	"""
	tree_scores = []
	for y in range(len(data)):
		for x in range(len(data[y])):
			tree_scores.append(visibleFromTree((x, y)))
	return max(tree_scores)


if __name__ == "__main__":
	print("part 1: ", part1())
	print("part 2: ", part2())
