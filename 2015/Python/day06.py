"""Day 06 Advent_of_Code 2015"""
with open("input/day06.txt", 'r') as infile:
	data = [line.rstrip().rsplit(' ', 3) for line in infile]  # split the strings
data = [[line[0], line[1].split(','), line[3].split(',')] for line in data]  # split coord strings and omit line[2]
# convert coordinates to integer tuples
data = [[line[0], tuple(int(n) for n in line[1]), tuple(int(n) for n in line[2])] for line in data]
light_grid = [[False for _ in range(1000)] for _ in range(1000)]  # create grid of off lights


def process_range(mode, coord1, coord2):
	x1, y1 = coord1
	x2, y2 = coord2
	match mode:
		case "turn on":
			for x in range(x1, x2+1):
				for y in range(y1, y2+1):
					light_grid[x][y] = True
		case "turn off":
			for x in range(x1, x2 + 1):
				for y in range(y1, y2 + 1):
					light_grid[x][y] = False
		case "toggle":
			for x in range(x1, x2 + 1):
				for y in range(y1, y2 + 1):
					light_grid[x][y] = not light_grid[x][y]
	return


if __name__ == "__main__":
	for instruction in data:
		process_range(*instruction)
	light_sum = 0
	for row in light_grid:
		light_sum += row.count(True)
	print("part 1: ", light_sum)
	# print("part 2: ")
