"""Day 09 Advent_of_Code 2025"""
with open("input/day09.txt", 'r') as infile:
	data = [list(map(int, line.rstrip().split(','))) for line in infile]


def rectArea(coordinate1, coordinate2):
	length = abs(coordinate1[0] - coordinate2[0]) + 1
	width = abs(coordinate1[1] - coordinate2[1]) + 1
	return length * width


def part1():
	area = 0
	for index in range(len(data)-1):
		for index2 in range(len(data[index:])):
			rectangle = rectArea(data[index], data[index2])
			if area < rectangle:
				area = rectangle
	return area


if __name__ == "__main__":
	print(data)
	print("part 1: ", part1())
	# print("part 2: ")
