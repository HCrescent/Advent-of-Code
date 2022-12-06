"""Day 06 Advent_of_Code 2022"""
with open("input/day06.txt", 'r') as infile:
	data = [line.rstrip() for line in infile]


def firstUniques(capture):
	for i in range(len(data[0])):
		detector_set = {each for each in data[0][i:i+capture]}
		if len(detector_set) == capture:
			return i+capture


if __name__ == "__main__":
	print("part 1: ", firstUniques(4))
	print("part 2: ", firstUniques(14))
