"""Day 02 Advent_of_Code 2017"""
with open("input/day02.txt", 'r') as infile:
	data = [list(map(int, line.rstrip().split("\t"))) for line in infile]


def part1():
	checksum = 0
	for row in data:
		checksum += max(row) - min(row)
	return checksum


def part2():
	checksum = 0
	for row in data:
		row.sort(reverse=True)
		for i, current in enumerate(row):
			for each in row[i+1:]:
				if current % each == 0:
					checksum += current//each
	return checksum

if __name__ == "__main__":
	print("part 1: ", part1())
	print("part 2: ", part2())
