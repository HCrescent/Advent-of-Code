"""Day 22 Advent_of_Code 2022"""
with open("input/day22.txt", 'r') as infile:
	data = infile.read().split('\n\n')
directions = data.pop().rstrip()
paces = [int(each) for each in directions.replace('R', 'L').split('L')]
left_right = [char for char in directions if char.isalpha()]
forest_map = data[0].split('\n')
forest_map = [[char for char in row] for row in forest_map]
real_space = {'.', '#'}
turn = {
	'L': {'^': '<', '<': 'v', 'v': '>', '>': '^'},
	'R': {'^': '>', '<': '^', 'v': '<', '>': 'v'}
}
move = {'^': (0, -1), '<': (-1, 0), 'v': (0, 1), '>': (1, 0)}
start_coord = (data[0].index('.'), 0)
walls = set()
for y in range(len(forest_map)):
	for x in range(len(forest_map[y])):
		if forest_map[y][x] == '#':
			walls.add((x, y))
score = {'>': 0, 'v': 1, '<': 2, '^': 3}
path = set(start_coord)  # just in case we want to make a nice visual representation later


def walk():
	def subFun():
		return
	cardinal = '>'  # cardinal will be the orientation we are facing
	current = list(start_coord)  # current will be our location before the walk step
	for i, steps in enumerate(paces):  # for each instruction steps + turn
		for _ in range(steps):  # for each in the integer number of steps
			# next find the proper coordinate we want to move to
			# temp coord is the current coord plus the proper cardinal adjustment
			tmp_x, tmp_y = [sum(coord) for coord in zip(current, move[cardinal])]
			# exception handles wrap cases
			try:
				# treat whitespace tiles as index errors for less redundant case coverage
				if forest_map[tmp_y][tmp_x] == ' ' or tmp_y < 0 or tmp_x < 0:
					raise IndexError
			except IndexError:
				match cardinal:
					case '<':  # exiting left coming in right
						# we want our x to be the rightmost edge, minus 1 for zero indexing
						tmp_x = len(forest_map[tmp_y])-1
					case '>':  # exiting right coming in left
						# left most element that is not a whitespace could be either '.' or '#'
						tmp_x = min(forest_map[tmp_y].index('.'), forest_map[tmp_y].index('#'))
					case '^':  # exiting top and coming in bottom
						# for each row from bottom to top, find the first y level that's a '.' or '#'
						for row in range(len(forest_map))[::-1]:
							try:  # if index error or whitespace we go on to next row
								if forest_map[row][tmp_x] in real_space:
									tmp_y = row
									break  # don't overwrite first find
							except IndexError:
								continue
					case 'v':  # exiting bottom and coming in top
						for row in range(len(forest_map)):
							try:  # if index error or whitespace we go on to next row
								if forest_map[row][tmp_x] in real_space:
									tmp_y = row
									break  # don't overwrite fist find
							except IndexError:
								continue
			# temporary coordinate to check if is a wall
			tmp_coord = [tmp_x, tmp_y]
			if tuple(tmp_coord) in walls:
				break
			current = tmp_coord
			# for row, each in enumerate(forest_map):
			# 	if row == current[1]:
			# 		tmp_char = forest_map[row][current[0]]
			# 		each[current[0]] = '@'
			# 	print("".join(each))
			# 	if row == current[1]:
			# 		each[current[0]] = tmp_char
			# print()
		cardinal = turn[left_right[i]][cardinal]
		if i == len(left_right)-1:
			break
	current[0] += 1
	current[1] += 1

	# given we found the correct end space and orientation, calculate the answer
	answer = 1000 * current[1]
	answer2 = 4 * current[0]
	answer3 = score[cardinal]
	summation = answer+answer2+answer3
	return summation


if __name__ == "__main__":
	print("part 1: ", walk())
	# print("part 2: ")
