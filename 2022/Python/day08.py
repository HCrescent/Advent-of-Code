"""Day 08 Advent_of_Code 2022"""
with open("input/day08.txt", 'r') as infile:
	data = [line.rstrip() for line in infile]
matrix = [[int(each) for each in line] for line in data]


def fun(grid):
	for each in grid:
		print(each)


def treeVisible(grid, height, coord):
	x, y = coord
	# if x == 3:
	# 	if y == 3:
	# 		print("h")
	for sub_x in range(x): # left side
		if grid[y][sub_x] >= height:
			break
	else:
		return True
	for sub_x in range(x+1, len(grid[y])):  # right side
		if grid[y][sub_x] >= height:
			break
	else:
		return True
	for sub_y in range(y):  # north direction
		if grid[sub_y][x] >= height:
			break
	else:
		return True
	for sub_y in range(y+1, len(grid)):  # south direction
		if grid[sub_y][x] >= height:
			break
	else:
		return True
	return False


def countVisTreesOut(grid):
	visible_trees_out = set()
	y_edge = len(grid)-1
	x_edge = len(grid[0])-1
	count = 1  # outside edge
	for y, row in enumerate(grid):
		for x, each in enumerate(grid[y]):
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
			tree_height = grid[y][x]
			if treeVisible(grid, tree_height, (x, y)):
				visible_trees_out.add((x, y))
	return len(visible_trees_out)


# for x, each in enumerate(grid[y]):
# 	match y:
# 		case 0:  # all top trees are visible
# 			visible_trees.add((x, y))
# 			continue
# 		case yEdge:  # all bottom trees are visible
# 			visible_trees.add((x, y))
# 			continue
# 	match x:
# 		case 0:  # all left edge trees are visible
# 			visible_trees.add((x, y))
# 			continue
# 		case x_edge:  # all right edge trees are visible
# 			visible_trees.add((x, y))
if __name__ == "__main__":
	# fun(matrix)
	print("part 1: ", countVisTreesOut(matrix))
	# print("part 2: ")
