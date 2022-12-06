"""Day 06 Advent_of_Code 2022"""
with open("input/day06.txt", 'r') as infile:
	data = [line.rstrip() for line in infile]


def part1():
	for i in range(len(data[0])):
		detector_set = {each for each in data[0][i:i+4]}
		if len(detector_set) == 4:
			return i+4


def part2():
	for i in range(len(data[0])):
		detector_set = {each for each in data[0][i:i+14]}
		if len(detector_set) == 14:
			return i+14


if __name__ == "__main__":
	print("part 1: ", part1())
	print("part 2: ", part2())
