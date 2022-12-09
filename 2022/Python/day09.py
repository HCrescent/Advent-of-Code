"""Day 09 Advent_of_Code 2022"""
with open("input/day09.txt", 'r') as infile:
	data = [(each[0], int(each[1])) for each in [line.rstrip().split(" ") for line in infile]]


def lagT(t, h):
	tx, ty = t
	hx, hy = h
	x_delta = abs(tx - hx)
	y_delta = abs(ty - hy)
	if x_delta == 2 and y_delta == 0:
		if hx < tx:
			t[0] -= 1
		else:
			t[0] += 1
	if y_delta == 2 and x_delta == 0:
		if hy < ty:
			t[1] -= 1
		else:
			t[1] += 1
	if x_delta == 2 and y_delta == 1:
		if tx < hx:
			t[0] += 1
		else:
			t[0] -= 1
		if ty < hy:
			t[1] += 1
		else:
			t[1] -= 1
	if y_delta == 2 and x_delta == 1:
		if ty < hy:
			t[1] += 1
		else:
			t[1] -= 1
		if tx < hx:
			t[0] += 1
		else:
			t[0] -= 1
	if y_delta == 2 and x_delta == 2:
		if ty < hy:
			t[1] += 1
		else:
			t[1] -= 1
		if tx < hx:
			t[0] += 1
		else:
			t[0] -= 1
	return t


def part1(moves):
	visited_coord = []
	H = [0, 0]
	T = [0, 0]
	for i, movement in enumerate(moves):
		match movement[0]:
			case 'R':
				for _ in range(movement[1]):
					H[0] += 1
					T = lagT(T, H)
					visited_coord.append(tuple(T))
			case 'L':
				for _ in range(movement[1]):
					H[0] -= 1
					T = lagT(T, H)
					visited_coord.append(tuple(T))
			case 'U':
				for _ in range(movement[1]):
					H[1] += 1
					T = lagT(T, H)
					visited_coord.append(tuple(T))
			case 'D':
				for _ in range(movement[1]):
					H[1] -= 1
					T = lagT(T, H)
					visited_coord.append(tuple(T))
	return len(set(visited_coord))


def part2(moves):
	rope_history = {each: [] for each in range(10)}
	rope_visited = {each: [] for each in range(10)}
	rope_coord = {each: [0, 0] for each in range(10)}
	for i, movement in enumerate(moves):
		match movement[0]:
			case 'R':
				for _ in range(movement[1]):
					rope_coord[0][0] += 1
					for rope in range(len(rope_coord)-1):
						rope_history[rope].append(tuple(rope_coord[rope]))
						rope_coord[rope+1] = lagT(rope_coord[rope+1], rope_coord[rope])
						rope_visited[rope+1].append(tuple(rope_coord[rope+1]))
			case 'L':
				for _ in range(movement[1]):
					rope_coord[0][0] -= 1
					for rope in range(len(rope_coord) - 1):
						rope_history[rope].append(tuple(rope_coord[rope]))
						rope_coord[rope + 1] = lagT(rope_coord[rope + 1], rope_coord[rope])
						rope_visited[rope + 1].append(tuple(rope_coord[rope + 1]))
			case 'U':
				for _ in range(movement[1]):
					rope_coord[0][1] += 1
					for rope in range(len(rope_coord) - 1):
						rope_history[rope].append(tuple(rope_coord[rope]))
						rope_coord[rope + 1] = lagT(rope_coord[rope + 1], rope_coord[rope])
						rope_visited[rope + 1].append(tuple(rope_coord[rope + 1]))
			case 'D':
				for _ in range(movement[1]):
					rope_coord[0][1] -= 1
					for rope in range(len(rope_coord) - 1):
						rope_history[rope].append(tuple(rope_coord[rope]))
						rope_coord[rope + 1] = lagT(rope_coord[rope + 1], rope_coord[rope])
						rope_visited[rope + 1].append(tuple(rope_coord[rope + 1]))
	return len(set(rope_visited[9]))


if __name__ == "__main__":
	print("part 1: ", part1(data))
	print("part 2: ", part2(data))
