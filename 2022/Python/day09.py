"""Day 09 Advent_of_Code 2022"""
import time
start = time.time()
with open("input/day09.txt", 'r') as infile:
	data = [(each[0], int(each[1])) for each in [line.rstrip().split(" ") for line in infile]]


def lagT(t, h):
	""" determines the tail movement for a head piece of simulated rope

	:param t: - List - [int, int]
	:param h: - List - [int, int]
	:return: - List - updated t parameter (or not changed if no movement required)
	"""
	tx, ty = t  # tail coordinate
	hx, hy = h  # head coordinate
	x_delta = abs(tx - hx)
	y_delta = abs(ty - hy)
	if x_delta == 2 and y_delta == 0:   # horizontal movements
		if tx < hx:
			t[0] += 1
		else:
			t[0] -= 1
		return t  # return updated tail coordinate
	if y_delta == 2 and x_delta == 0:  # vertical movements
		if ty < hy:
			t[1] += 1
		else:
			t[1] -= 1
		return t  # return updated tail coordinate
	if x_delta + y_delta < 3:  # for all cases with no move
		return t  # return unchanged tail coordinate
	# for all cases resulting in diagonal movements
	if tx < hx:
		t[0] += 1
	else:
		t[0] -= 1
	if ty < hy:
		t[1] += 1
	else:
		t[1] -= 1
	return t  # return updated tail coordinate


def simulateRopes(moves, total_ropes):
	""" takes the input movement data and a number of rope segments, then simulates the movement of all rope
	segments given the head ends movements.

	:param moves: List - [str, int] - list of movements in input data
	:param total_ropes: Int - number of attached rope segments
	:return: Int - the total number of unique space visited by tail segment
	"""
	rope_visited = {each: [] for each in range(total_ropes)}
	rope_coord = {each: [0, 0] for each in range(total_ropes)}
	for movement in moves:
		match movement[0]:
			case 'R':
				for _ in range(movement[1]):  # repeat for number of times given for direction
					rope_coord[0][0] += 1  # move lead rope right one unit
					for rope in range(len(rope_coord)-1):  # for each rope minus the first
						rope_coord[rope+1] = lagT(rope_coord[rope+1], rope_coord[rope])
						if rope == total_ropes-2:  # remove check if you want data for each rope segment segment
							rope_visited[rope+1].append(tuple(rope_coord[rope+1]))
			case 'L':
				for _ in range(movement[1]):
					rope_coord[0][0] -= 1  # move lead rope left one unit
					for rope in range(len(rope_coord)-1):  # for each rope minus the first
						rope_coord[rope+1] = lagT(rope_coord[rope+1], rope_coord[rope])
						if rope == total_ropes - 2:  # remove check if you want data for each rope segment segment
							rope_visited[rope+1].append(tuple(rope_coord[rope+1]))
			case 'U':
				for _ in range(movement[1]):
					rope_coord[0][1] += 1  # move lead rope up one unit
					for rope in range(len(rope_coord)-1):  # for each rope minus the first
						rope_coord[rope+1] = lagT(rope_coord[rope+1], rope_coord[rope])
						if rope == total_ropes - 2:  # remove check if you want data for each rope segment segment
							rope_visited[rope+1].append(tuple(rope_coord[rope+1]))
			case 'D':
				for _ in range(movement[1]):
					rope_coord[0][1] -= 1  # move lead rope down one unit
					for rope in range(len(rope_coord)-1):  # for each rope minus the first
						rope_coord[rope+1] = lagT(rope_coord[rope+1], rope_coord[rope])
						if rope == total_ropes - 2:  # remove check if you want data for each rope segment segment
							rope_visited[rope+1].append(tuple(rope_coord[rope+1]))
	return len(set(rope_visited[total_ropes-1]))  # total unique coordinates visited by the tail end of conjoined ropes


if __name__ == "__main__":
	print("part 1: ", simulateRopes(data, 2))
	print("part 2: ", simulateRopes(data, 10))
	end = time.time()
	print(f"t:{end - start}")
