"""Day 15 Advent_of_Code 2022"""
with open("input/day15.txt", 'r') as infile:
	data = [line.rstrip().split(": closest ") for line in infile]
sensors = [tuple(int(num) for num in each[0].replace("x=", "")[10:].replace("y=", "").split(', ')) for each in data]
beacons = [tuple(int(num) for num in each[1].replace("x=", "")[13:].replace("y=", "").split(', ')) for each in data]


def getDistance(sensor, beacon):
	return abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])


def condenseCoverage(ranges, part_1=True):
	""" takes a list of covered ranges and condenses them into the a simplified range or ranges, condensing overlap
	into single range if possible, multiple ranges if theres gaps

	:param ranges: List - list of scanned ranges
	:param part_1: Bool - flag to extend functionality to part2
	:return: List - simplified ranges
	"""
	unique_ranges = []  # the final spread to return
	temp_range = ranges[0]  # the range we are building arithmetically
	for each in ranges[1:]:
		if each[0] <= temp_range[1]:  # if left x-bound for each range, is contained inside our temp
			if each[1] > temp_range[1]:  # if it starts inside and extends farther, the new farthest is each[1]
				temp_range.pop()  # remove old right-bound
				temp_range.append(each[1])  # add new right-bound
		else:  # gap in coverage
			unique_ranges.append(temp_range)
			temp_range = each
	else:  # we went through all ranges
		unique_ranges.append(temp_range)
	if part_1:
		return unique_ranges
	unique_ranges_p2 = []
	left, right = 0, 4_000_000
	temp_range_p2 = []
	for each in unique_ranges:
		if each[0] < left <= each[1]:  # if zero is between left and right bound
			temp_range_p2.append(left)  # temp range starts at 0
			if each[1] >= right:  # if each[1] is greater or equal than right we are done
				temp_range_p2.append(right)  # right bound is 4 mil
				unique_ranges_p2.append(temp_range_p2)
				return unique_ranges_p2
			else:
				temp_range_p2.append(each[1])  # append the right bound
				unique_ranges_p2.append(temp_range_p2)  # put it in unique ranges part 2
		else:  # zero is not withing bound
			if each[1] >= right:
				unique_ranges_p2.append([each[0], right])
				return unique_ranges_p2


def knownSpaces(y_row):
	""" for a single y row gets a list of all scanned ranges on that 1D line

	:param y_row: Int - the row we want the scanned information from
	:return: List - ranges of scanned points on that y row
	"""
	manhattans = [getDistance(*pair) for pair in list(zip(sensors, beacons))]  # get all manhattan distance totals
	coverage_range = []
	for i, sensor in enumerate(sensors):
		delta_y = abs(sensor[1] - y_row)
		if delta_y > manhattans[i]:  # coverage does not reach
			continue
		else:  # coverage reaches at least 1 square
			x1, x2 = sensor[0] - manhattans[i] + delta_y, sensor[0] + manhattans[i] - delta_y
			coverage_range.append([x1, x2])
	return sorted(coverage_range)


def part1(target):
	ranges = knownSpaces(target)
	simplified_ranges = condenseCoverage(ranges)
	total = 0
	for each in simplified_ranges:
		total += (each[1] - each[0])+1
	return total - len(set([each for each in beacons if each[1] == target]))  # subtract beacons in that line


def part2():
	# bruteforce approach of running part 1 up to 4 million times, takes about 1 min to execute
	for i in range(4_000_001):
		ranges = knownSpaces(i)
		simplified_ranges = condenseCoverage(ranges, False)
		if len(simplified_ranges) > 1:
			x = simplified_ranges[0][1]+1
			y = i
			return x * 4_000_000 + y


if __name__ == "__main__":
	print("part 1: ", part1(2_000_000))
	print("part 2: ", part2())
