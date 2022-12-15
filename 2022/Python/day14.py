"""Day 14 Advent_of_Code 2022"""
from os import system, name
from time import sleep
with open("input/day14.txt", 'r') as infile:
	data = [[tuple(map(int, coord.split(","))) for coord in line.rstrip().split(" -> ")] for line in infile]


def clear():
	if name == 'nt':
		_ = system('cls')


def display(void_level, cavern_map, sand_map, time):
	max_x = max([each[0] for each in cavern_map])
	min_x = min([each[0] for each in cavern_map])
	matrix = [['.' for x in range(max_x+2)] for y in range(void_level+1)]
	matrix[0][500] = '+'
	matrix[time[1]][time[0]] = '0'
	for coord in cavern_map:
		matrix[coord[1]][coord[0]] = '#'
	for coord in sand_map:
		matrix[coord[1]][coord[0]] = 'O'
	for each in matrix:
		print("".join(each[min_x-1:max_x+3]))
	sleep(0.2)
	clear()
	return


def buildObstacles(directions):
	""" takes the input data and "Draws" the lines as a set of coordinates

	:param directions: List - list of continuous line drawing directives
	:return: Set - set of all coordinates of impassible obstacles
	"""
	coord_set = set()
	for line in directions:
		coord_set.add(line[0])  # the initial point, then we can always draw ending on the next point inclusive
		for i in range(len(line)-1):
			x1, y1 = line[i]
			x2, y2 = line[i+1]
			delta_x = abs(x1 - x2)
			delta_y = abs(y1 - y2)
			if delta_x:  # x coordinate changed
				# determine left or right direction
				if x1 < x2:
					for n in range(delta_x):
						coord_set.add((x2-n, y1))
				else:
					for n in range(delta_x):
						coord_set.add((x2+n, y1))
			elif delta_y:  # y coordinate changed
				# determine up or down direction
				if y1 < y2:
					for n in range(delta_y):
						coord_set.add((x1, y2-n))
				else:
					for n in range(delta_y):
						coord_set.add((x1, y2+n))
	return coord_set


def pourSand(void_level, cavern_map, source=(500, 0)):
	sand_map = set()
	sand = source
	movement_adjustment = ((0, 1), (-1, 1), (1, 1))  # movements down, left, right
	while sand[1] < void_level:
		sand = source
		while sand[1] < void_level:
			for adjust in movement_adjustment:
				move = (sand[0] + adjust[0], sand[1] + adjust[1])
				if move not in cavern_map and move not in sand_map:
					# display(void_level, cavern_map, sand_map, sand)  # for sample displaying
					sand = move
					break
			else:  # nowhere to go, sand found its resting spot
				sand_map.add(sand)
				break
	return sand_map


def pourSand2(floor_level, cavern_map, source=(500, 0)):
	sand_map = set()
	sand = source
	movement_adjustment = ((0, 1), (-1, 1), (1, 1))  # movements down, left, right
	while source not in sand_map:
		sand = source
		while source not in sand_map:
			for adjust in movement_adjustment:
				move = (sand[0] + adjust[0], sand[1] + adjust[1])
				if move not in cavern_map and move not in sand_map and move[1] < floor_level+1:
					sand = move
					break
			else:  # nowhere to go, sand found its resting spot
				sand_map.add(sand)
				break
	return sand_map


def mainDriver(part1=True):
	occupied_spaces = buildObstacles(data)  # get list of coordinates with impassable walls
	max_y = max([each[1] for each in occupied_spaces])+1  # get the y coordinate for the void
	if part1:
		sand_map = pourSand(max_y, occupied_spaces)
	else:
		sand_map = pourSand2(max_y, occupied_spaces)
	return len(sand_map)


if __name__ == "__main__":
	print("part 1: ", mainDriver())
	print("part 2: ", mainDriver(False))
