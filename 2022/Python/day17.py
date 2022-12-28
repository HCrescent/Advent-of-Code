"""Day 17 Advent_of_Code 2022"""
# from os import system, name
# from time import sleep
with open("input/day17.txt", 'r') as infile:
	data = infile.read().rstrip()
occupied_space = set(tuple((x, 0)) for x in range(9))
left_wall, right_wall = 0, 8
shapes = {
	0: lambda x, y: [[x, y], [x+1, y], [x+2, y], [x+3, y]],
	1: lambda x, y: [[x, y+1], [x+1, y+1], [x+1, y+2], [x+1, y], [x+2, y+1]],
	2: lambda x, y: [[x, y], [x+1, y], [x+2, y], [x+2, y+1], [x+2, y+2]],
	3: lambda x, y: [[x, y], [x, y+1], [x, y+2], [x, y+3]],
	4: lambda x, y: [[x, y], [x, y+1], [x+1, y], [x+1, y+1]]
}


def adjustRight(object_space):
	if max([coord[0] for coord in object_space]) < 7:
		for each in object_space:
			if (each[0]+1, each[1]) in occupied_space:
				return  # return without change, space occupied
		for i, each in enumerate(object_space):  # change original referenced object space
			object_space[i][0] += 1
	return


def adjustLeft(object_space):
	if min([coord[0] for coord in object_space]) > 1:
		for each in object_space:
			if (each[0]-1, each[1]) in occupied_space:
				return  # return without change, space occupied
		for i, each in enumerate(object_space):  # change original referenced object space
			object_space[i][0] -= 1
	return


def adjustDown(object_space):
	for each in object_space:
		if (each[0], each[1]-1) in occupied_space:  # reached resting spot
			for coord in object_space:
				occupied_space.add(tuple(coord))
			return False  # return false if we solidified
	for i, each in enumerate(object_space):  # change original referenced object space
		object_space[i][1] -= 1
	return True  # return true if move downwards was successful


def highestRock():
	return max([each[1] for each in occupied_space])


def part1(rock_total):
	jet = 0  # jet index
	mod = len(data)  # the length of data for repeating modulous
	for n in range(rock_total):
		tetromino = shapes[n % 5](3, highestRock()+4)
		if data[jet % mod] == '<':
			adjustLeft(tetromino)
		else:
			adjustRight(tetromino)
		jet += 1
		while adjustDown(tetromino):
			if data[jet % mod] == '<':
				adjustLeft(tetromino)
			else:
				adjustRight(tetromino)
			jet += 1
	return highestRock()


def part2(rock_total):
	global occupied_space  # so we can reinitialize the global scoped set
	occupied_space = set(tuple((x, 0)) for x in range(9))
	jet = 0  # jet index
	mod = len(data)  # the length of data for repeating modulous
	flag = True
	n = 0
	cycle_set = set()  # set of starting jet on first piece
	data_list = []  # list of data for getting deltas from our cycle analysis
	while flag:
		tetromino = shapes[n % 5](3, highestRock() + 4)
		if data[jet % mod] == '<':
			adjustLeft(tetromino)
		else:
			adjustRight(tetromino)
		jet += 1
		while adjustDown(tetromino):
			if data[jet % mod] == '<':
				adjustLeft(tetromino)
			else:
				adjustRight(tetromino)
			jet += 1
		n += 1
		if n % 5 == 0:  # for every first piece
			data_list.append([n, jet % mod, highestRock()])
			if jet % mod not in cycle_set:
				cycle_set.add(jet % mod)
			else:  # if we repeated flip the flag
				flag = False
	# acquire needed quantities for calculation based on cycle data
	delta_sublist = [each for each in data_list if each[1] == data_list[-1][1]]
	delta_rocks = delta_sublist[1][0] - delta_sublist[0][0]  # get delta number of rocks per cycle
	delta_height = delta_sublist[1][2] - delta_sublist[0][2]  # get height difference per cycle
	pre_cycle_count = delta_sublist[0][0]
	pre_cycle_height = delta_sublist[0][2]
	new_rock_total = rock_total - pre_cycle_count  # subtract the initial precycle rocks
	total_cycles_fit = new_rock_total // delta_rocks  # the number of cycles that fit into our total
	remainder_after_cycles = new_rock_total % delta_rocks
	new_height = (total_cycles_fit * delta_height) + pre_cycle_height
	extras_sub_list = [
		delta_sublist[0],
		[each for each in data_list if each[0] == delta_sublist[0][0] + remainder_after_cycles][0]
	]
	return new_height + extras_sub_list[1][2] - extras_sub_list[0][2]


# def clear():
# 	if name == 'nt':
# 		_ = system('cls')


# def display(object_map):
# 	max_x = 8
# 	min_x = 0
# 	max_y = highestRock()
# 	matrix = [['.' for _ in range(max_x+1)] for _ in range(max_y+5)]
# 	for y, row in enumerate(matrix):
# 		for x in range(len(row)):
# 			if x == min_x or x == max_x:
# 				matrix[y][x] = '|'
# 	for coord in object_map:
# 		matrix[coord[1]][coord[0]] = '#'
# 	# for coord in block_map:
# 	# 	matrix[coord[1]][coord[0]] = '@'
# 	clear()
# 	for i in range(9):
# 		if i == 0 or i == 8:
# 			matrix[0][i] = '+'
# 		else:
# 			matrix[0][i] = '-'
# 	for row in matrix[::-1]:
# 		print("".join(row))
# 	print()
# 	sleep(0.2)
# 	return


if __name__ == "__main__":
	print("part 1: ", part1(2022))
	print("part 2: ", part2(1_000_000_000_000))
