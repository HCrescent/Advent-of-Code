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


def walk():
	cardinal = '>'
	current = list(start_coord)
	forest_map[current[1]][current[0]] = cardinal
	print(current)
	for i, steps in enumerate(paces):  # for each instruction steps + turn
		for _ in range(steps):  # for each in the integer number of steps
			forest_map[current[1]][current[0]] = cardinal
			tmp_coord = [current[0] + move[cardinal][0], current[1] + move[cardinal][1]]
			if tuple(tmp_coord) in walls:
				break
			else:
				# wrapping logic
				try:
					if forest_map[tmp_coord[1]][tmp_coord[0]] == '':
						pass
				except IndexError:
					tmp_coord[0] = forest_map[tmp_coord[1]].index('.')
				current = tmp_coord
				for each in forest_map:
					print("".join(each))
				print()
		cardinal = turn[left_right[i]][cardinal]

	return


if __name__ == "__main__":
	for each in data:
		print(each)
	walk()
	# print("part 1: ")
	# print("part 2: ")
