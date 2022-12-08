"""Day 08 Advent_of_Code 2022"""
with open("input/day08.txt", 'r') as infile:
	data = [[int(each) for each in line.rstrip()] for line in infile]


def treeVisible(coord):
	x, y = coord
	height = data[y][x]
	for sub_x in range(x):  # left side
		if data[y][sub_x] >= height:
			break
	else:  # didn't break: Tree visible from outside
		return True
	for sub_x in range(x+1, len(data[y])):  # right side
		if data[y][sub_x] >= height:
			break
	else:  # didn't break: Tree visible from outside
		return True
	for sub_y in range(y):  # north direction
		if data[sub_y][x] >= height:
			break
	else:  # didn't break: Tree visible from outside
		return True
	for sub_y in range(y+1, len(data)):  # south direction
		if data[sub_y][x] >= height:
			break
	else:  # didn't break: Tree visible from outside
		return True
	return False  # got here: tree is not visible


def countVisTreesOut():
	visible_trees_out = set()
	y_edge = len(data)-1
	x_edge = len(data[0])-1
	count = 1  # outside edge
	for y, row in enumerate(data):
		for x, each in enumerate(data[y]):
			if y == 0:  # all top trees are visible
				visible_trees_out.add((x, y))
				continue
			elif y == y_edge:  # all bottom trees are visible
				visible_trees_out.add((x, y))
				continue
			if x == 0:  # all left edge trees are visible
				visible_trees_out.add((x, y))
				continue
			elif x == x_edge:  # all right edge trees are visible
				visible_trees_out.add((x, y))
				continue
			if treeVisible((x, y)):
				visible_trees_out.add((x, y))
	return len(visible_trees_out)


def visibleFromTree(coord):
	x, y = coord
	height = data[y][x]
	countN, countS, countE, countW = 0, 0, 0, 0
	for sub_x in range(x)[::-1]:  # left side
		if data[y][sub_x] >= height:
			countW += 1
			break
		else:
			countW += 1
	for sub_x in range(x+1, len(data[y])):  # right side
		if data[y][sub_x] >= height:
			countE +=1
			break
		else:
			countE += 1
	for sub_y in range(y)[::-1]:  # north direction
		if data[sub_y][x] >= height:
			countN += 1
			break
		else:
			countN += 1
	for sub_y in range(y+1, len(data)):  # south direction
		if data[sub_y][x] >= height:
			countS += 1
			break
		else:
			countS += 1
	return countN * countW * countE * countS


def part2():
	tree_scores = []
	for y in range(len(data)):
		for x in range(len(data[y])):
			tree_scores.append(visibleFromTree((x, y)))
	return max(tree_scores)


if __name__ == "__main__":
	print("part 1: ", countVisTreesOut())
	print("part 2: ", part2())
