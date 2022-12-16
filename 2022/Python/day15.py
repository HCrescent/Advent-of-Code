"""Day 15 Advent_of_Code 2022"""
with open("input/day15.txt", 'r') as infile:
	data = [line.rstrip().split(": closest ") for line in infile]
sensors = [tuple(int(num) for num in each[0].replace("x=", "")[10:].replace("y=", "").split(', ')) for each in data]
beacons = [tuple(int(num) for num in each[1].replace("x=", "")[13:].replace("y=", "").split(', ')) for each in data]


def getDistance(sensor, beacon):
	return abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])


def part1(y_row):
	row_dict = {}
	movements = []
	for i, sensor in enumerate(sensors):
		dist = getDistance(sensor, beacons[i])
		x, y = sensor
		current = [x, y-dist]  # top of area
		# top triangle section
		for N in range(dist):
			current[1] = y + (N-dist)
			if current[1] in row_dict:
				row_dict[current[1]].add(tuple(current))  # add coordinate to that rows dict set
			else:
				row_dict.update({current[1]: set()})  # make new entry in dict with a set initialized with coord
				row_dict[current[1]].add((current[0], current[1]))
			# left side squares
			for left in range(1, N+1):
				row_dict[current[1]].add((current[0]-left, current[1]))  # add spaces to left of current
			# right side squares
			for right in range(1, N+1):
				row_dict[current[1]].add((current[0]+right, current[1]))  # add spaces to right of current
		# bottom triangle section
		current = [x, y+dist]
		for N in range(dist):
			current[1] = y - (N-dist)
			if current[1] in row_dict:
				row_dict[current[1]].add(tuple(current))  # add coordinate to that rows dict set
			else:
				row_dict.update({current[1]: set()})  # make new entry in dict with a set initialized with coord
				row_dict[current[1]].add((current[0], current[1]))
			# left side squares
			for left in range(1, N + 1):
				row_dict[current[1]].add((current[0] - left, current[1]))  # add spaces to left of current
			# right side squares
			for right in range(1, N + 1):
				row_dict[current[1]].add((current[0] + right, current[1]))  # add spaces to right of current
		# middle base line
		current = [x, y]
		for N in range(dist+1):
			if current[1] in row_dict:
				row_dict[current[1]].add(tuple(current))  # add coordinate to that rows dict set
			else:
				row_dict.update({current[1]: set()})  # make new entry in dict with a set initialized with coord
				row_dict[current[1]].add((current[0], current[1]))
			# left side squares
			for left in range(1, N + 1):
				row_dict[current[1]].add((current[0] - left, current[1]))  # add spaces to left of current
			# right side squares
			for right in range(1, N + 1):
				row_dict[current[1]].add((current[0] + right, current[1]))  # add spaces to right of current
	return len(row_dict[y_row])


if __name__ == "__main__":
	print("part 1: ", part1(2_000_000))
	# print("part 2: ")
