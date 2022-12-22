"""Day 22 Advent_of_Code 2022"""
with open("input/day22.txt", 'r') as infile:
	data = infile.read().split('\n\n')
directions = data.pop().rstrip()
paces = [int(each) for each in directions.replace('R', 'L').split('L')]
left_right = [char for char in directions if char.isalpha()]
forest_map = data[0].split('\n')
forest_map = [[char for char in row] for row in forest_map]

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


def walk():
	cardinal = '>'
	current = list(start_coord)
	# forest_map[current[1]][current[0]] = cardinal
	# print(current)
	# for c, v in enumerate(paces):
	# 	print(c, v)
	# print(len(paces))
	# print(len(left_right))
	for i, steps in enumerate(paces):  # for each instruction steps + turn
		for _ in range(steps):  # for each in the integer number of steps
			try:
				if forest_map[current[1]][current[0]] != '.':
					print(current)
			except IndexError:
				print(current)
				for each in forest_map[current[1]-5:current[1]+6]:
					print("".join(each))
				raise exit(1)
			tmp_coord = [current[0] + move[cardinal][0], current[1] + move[cardinal][1]]
			# wrapping logic
			try:
				if forest_map[tmp_coord[1]][tmp_coord[0]] == ' ':
					tmp_x = tmp_coord[0]
					tmp_y = tmp_coord[1]
					if cardinal == 'v':
						for row in range(len(forest_map)):
							if forest_map[row][tmp_x] != ' ':
								tmp_coord = [tmp_x, row]
								break
					if cardinal == '^':
						for row in range(len(forest_map))[::-1]:
							if forest_map[row][tmp_x] != ' ':
								tmp_coord = [tmp_x, row]
								break
					if cardinal == '<':
						tmp_coord[0] = len(forest_map[tmp_coord[1]]) - 1
			except IndexError:
				if cardinal == '>':
					tmp_coord[0] = forest_map[tmp_coord[1]].index('.')
				if cardinal == '<':
					tmp_coord[0] = len(forest_map[tmp_coord[1]])-1
				if cardinal == '^':
					for row_i in range(len(forest_map))[::-1]:
						try:
							if forest_map[row_i][tmp_coord[0]] != " ":
								tmp_coord[1] = row_i
								break
						except IndexError:
							tmp_coord[1] = row_i-1
				if cardinal == 'v':
					for row_i in range(len(forest_map)):
						if forest_map[row_i][tmp_coord[0]] != " ":
							tmp_coord[1] = row_i
							break
			if tuple(tmp_coord) in walls:
				break
			current = tmp_coord
			# for each in forest_map:
			# 	print("".join(each))
			# print()
		cardinal = turn[left_right[i]][cardinal]
		if i == len(left_right)-1:
			break
	current[0] += 1
	current[1] += 1
	answer = 1000 * current[1]
	answer2 = 4 * current[0]
	answer3 = score[cardinal]
	summation = answer+answer2+answer3
	return summation


if __name__ == "__main__":
	print(walk())
	# print("part 1: ")
	# print("part 2: ")
