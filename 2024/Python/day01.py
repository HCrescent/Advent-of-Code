"""Day 01 Advent_of_Code 2024"""
with open("input/day01.txt", 'r') as infile:
	data = [list(map(int, line.rstrip().split())) for line in infile]


def part1():
	left = [each[0] for each in data]
	right = [each[1] for each in data]
	left.sort()
	right.sort()
	delta = 0
	for i, each in enumerate(left):
		delta += abs(each - right[i])
	return delta


def part2():
	left = [each[0] for each in data]
	right = [each[1] for each in data]
	total = 0
	for i, each in enumerate(left):
		total+= each * right.count(each)
	return total


if __name__ == "__main__":
	print("part 1: ", part1())
	print("part 2: ", part2())
