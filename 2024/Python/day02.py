"""Day 02 Advent_of_Code 2024"""
with open("input/day02.txt", 'r') as infile:
	data = [list(map(int, line.rstrip().split())) for line in infile]


def safe(test_list):
	result = False
	parity = 0
	if test_list[0] > test_list[1]:
		parity = -1
	elif test_list[0] < test_list[1]:
		parity = 1
	# decreasing
	if parity == -1:
		for i in range(len(test_list)-1):
			delta = test_list[i] - test_list[i+1]
			if (delta < 1) | (delta > 3):
				break
		else:
			result = True
	# increasing
	if parity == 1:
		for i in range(len(test_list)-1):
			delta = test_list[i] - test_list[i+1]
			if (delta < -3) | (delta > -1):
				break
		else:
			result = True
	return result


def almost_safe(test_list):
	for i in range(len(test_list)):
		if safe(test_list[:i] + test_list[i+1:]):
			return True
	else:
		return False


def part1():
	safeTotal = 0
	for each in data:
		if safe(each):
			safeTotal += 1
	return safeTotal


def part2():
	safeTotal = 0
	for each in data:
		if almost_safe(each):
			safeTotal += 1
	return safeTotal


if __name__ == "__main__":
	print("part 1: ", part1())
	print("part 2: ", part2())
