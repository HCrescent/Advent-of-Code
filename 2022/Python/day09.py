"""Day 09 Advent_of_Code 2022"""
with open("input/day09.txt", 'r') as infile:
	data = [(each[0], int(each[1])) for each in [line.rstrip().split(" ") for line in infile]]


def lagT(t, h, last_position):
	tx, ty = t
	hx, hy = h
	x_delta = abs(tx - hx)
	y_delta = abs(ty - hy)
	if x_delta == 2 or y_delta == 2:
		return last_position
	else:
		return t


def part1(moves):
	visited_coord = []
	h_history = []
	H = [0, 0]
	T = [0, 0]
	for i, movement in enumerate(moves):
		match movement[0]:
			case 'R':
				for _ in range(movement[1]):
					h_history.append(tuple(H))
					H[0] += 1
					T = lagT(T, H, h_history[-1])
					visited_coord.append(tuple(T))
			case 'L':
				for _ in range(movement[1]):
					h_history.append(tuple(H))
					H[0] -= 1
					T = lagT(T, H, h_history[-1])
					visited_coord.append(tuple(T))
			case 'U':
				for _ in range(movement[1]):
					h_history.append(tuple(H))
					H[1] += 1
					T = lagT(T, H, h_history[-1])
					visited_coord.append(tuple(T))
			case 'D':
				for _ in range(movement[1]):
					h_history.append(tuple(H))
					H[1] -= 1
					T = lagT(T, H, h_history[-1])
					visited_coord.append(tuple(T))
	return len(set(visited_coord))


def part2():
	rope_dict = {each: [0, 0] for each in range(10)}

if __name__ == "__main__":
	print("part 1: ", part1(data))
	# print("part 2: ")
