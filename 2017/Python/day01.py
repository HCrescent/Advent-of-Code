"""Day 01 Advent_of_Code 2017"""
with open("input/day01.txt", 'r') as infile:
	data = [line.rstrip() for line in infile][0]


def part1():
	total = 0
	for i in range(len(data)-1):
		if data[i] == data[i+1]:
			total += int(data[i])
	if data[-1] == data[0]:
		total += int(data[0])
	return total


def part2():
	total = 0
	width = len(data)
	for i in range(width):
		if data[i] == data[(i+width//2) % width]:
			total += int(data[i])
	return total


if __name__ == "__main__":
	print("part 1: ", part1())
	print("part 2: ", part2())
