"""Day 11 Advent_of_Code 2021"""
with open("input/day11.txt", 'r') as infile:
	data = [list(map(int, line.rstrip())) for line in infile]


def increment_matrix():
	"""Increments the entire matrix by 1, then goes on to call the rest of the functions needed per step.

	:return: int - number of flashes that occurred in the finished step.
	"""
	# initialize our record dict for processed entries and make sure the loop in process_dumbo() starts true
	record = {"delta": 1}
	for x in range(len(data)):
		for y in range(len(data[x])):
			data[x][y] += 1
	record = process_dumbo(record)
	flashes = flash_dumbo(record)
	return flashes


def process_dumbo(record):
	"""Iterates over the matrix processing each overcharged oct's surrounding neighbors. repeating for new overcharges.

	:param record: dict - our record of processed elements to prevent re-processing on delta passes
	:return: dict - updated record to be passed back to flash_dumbo for
	"""
	# initialize our record dict for processed entries and make sure the loop starts true

	# while number of delta entries (new flashing octopuses) is greater than zero
	while record["delta"] > 0:
		record["delta"] = 0
		for x in range(len(data)):
			for y in range(len(data[x])):
				if record.get(f"m:{x},{y}", 1):
					record = energy_increment(x, y, record)
	return record


def flash_dumbo(record):
	"""Takes all the over energized octopuses and rolls them over to zero.

	:param record: dict - our record of processed elements to prevent re-processing on delta passes
	:return: int - number of entries in our record dict
	"""
	for x in range(len(data)):
		for y in range(len(data[x])):
			if f"m:{x},{y}" in record:
				data[x][y] = 0
	return len(record) - 1


def steps():
	"""Simulates the octopuses one step at a time, returning the total flashes at step 100, exits on full sync.

	"""
	step = 1
	flash = []
	while True:
		flash.append(increment_matrix())
		if step == 100:
			print("part 1: ", sum(flash))
		if flash[-1] == len(data) * len(data[0]):
			print("part 2: ", step)
			exit(1)
		step += 1
	pass


def energy_increment(x, y, record):
	"""Takes a Coordinate and increments its surrounding neighbors, adds key to record, only if our co-ord is over 9.

	:param x: int - x co-ord
	:param y: int - y co-ord
	:param record: dict - our record of processed elements to prevent re-processing on delta passes
	:return: dict - the updated record of processed elements
	"""
	match x, y:
		# case for data[x][y] has 8 neighbors.
		case x, y if 0 < x < len(data)-1 and 0 < y < len(data[x])-1 and data[x][y] > 9:
			record[f"m:{x},{y}"] = False
			record["delta"] += 1
			data[x-1][y] += 1    # north
			data[x-1][y+1] += 1  # north-east
			data[x][y+1] += 1    # east
			data[x+1][y+1] += 1  # south-east
			data[x+1][y] += 1    # south
			data[x+1][y-1] += 1  # south-west
			data[x][y-1] += 1    # west
			data[x-1][y-1] += 1  # north-west
	# top edge case, always 5 neighbors: east, south-east, south, south-west, west
		case x, y if x == 0 and 0 < y < len(data[x])-1 and data[x][y] > 9:
			record[f"m:{x},{y}"] = False
			record["delta"] += 1
			data[x][y+1] += 1    # east
			data[x+1][y+1] += 1  # south-east
			data[x+1][y] += 1    # south
			data[x+1][y-1] += 1  # south-west
			data[x][y-1] += 1    # west
		# right edge case, always 5 neighbors: north, south, south-west, west, north-west
		case x, y if 0 < x < len(data)-1 and y == len(data[x])-1 and data[x][y] > 9:
			record[f"m:{x},{y}"] = False
			record["delta"] += 1
			data[x-1][y] += 1    # north
			data[x+1][y] += 1    # south
			data[x+1][y-1] += 1  # south-west
			data[x][y-1] += 1    # west
			data[x-1][y-1] += 1  # north-west
		# bottom edge case, always 5 neighbors: north, north-east, east, west, north-west
		case x, y if x == len(data)-1 and 0 < y < len(data[x])-1 and data[x][y] > 9:
			record[f"m:{x},{y}"] = False
			record["delta"] += 1
			data[x-1][y] += 1    # north
			data[x-1][y+1] += 1  # north-east
			data[x][y+1] += 1    # east
			data[x][y-1] += 1    # west
			data[x-1][y-1] += 1  # north-west
		# left edge case, always 5 neighbors: north, north-east, east, south-east, south
		case x, y if 0 < x < len(data)-1 and y == 0 and data[x][y] > 9:
			record[f"m:{x},{y}"] = False
			record["delta"] += 1
			data[x-1][y] += 1    # north
			data[x-1][y+1] += 1  # north-east
			data[x][y+1] += 1    # east
			data[x+1][y+1] += 1  # south-east
			data[x+1][y] += 1    # south
		# top left corner case, always 3 neighbors: east, south-east, south
		case x, y if x == 0 and y == 0 and data[x][y] > 9:
			record[f"m:{x},{y}"] = False
			record["delta"] += 1
			data[x][y+1] += 1    # east
			data[x+1][y+1] += 1  # south-east
			data[x+1][y] += 1    # south
		# top right corner case, always 3 neighbors: south, south-west, west
		case x, y if x == 0 and y == len(data[x])-1 and data[x][y] > 9:
			record[f"m:{x},{y}"] = False
			record["delta"] += 1
			data[x+1][y] += 1    # south
			data[x+1][y-1] += 1  # south-west
			data[x][y-1] += 1    # west
		# bottom left corner case, always 3 neighbors: north, north-east, east
		case x, y if x == len(data)-1 and y == 0 and data[x][y] > 9:
			record[f"m:{x},{y}"] = False
			record["delta"] += 1
			data[x-1][y] += 1    # north
			data[x-1][y+1] += 1  # north-east
			data[x][y+1] += 1    # east
		# bottom right corner case, always 3 neighbors: west, north-west, north
		case x, y if x == len(data)-1 and y == len(data[x])-1 and data[x][y] > 9:
			record[f"m:{x},{y}"] = False
			record["delta"] += 1
			data[x][y-1] += 1    # west
			data[x-1][y-1] += 1  # north-west
			data[x-1][y] += 1    # north
	return record


if __name__ == "__main__":
	steps()
