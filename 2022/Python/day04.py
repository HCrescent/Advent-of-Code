"""Day 04 Advent_of_Code 2022"""
with open("input/day04.txt", 'r') as infile:
	data = [line.rstrip().split(',') for line in infile]


def part1():
	count = 0
	for line in data:
		start, end = map(int, line[0].split('-'))
		elf1_set = {_ for _ in range(start, end+1)}
		start, end = map(int, line[1].split('-'))
		elf2_set = {_ for _ in range(start, end+1)}
		if elf1_set.issubset(elf2_set) or elf2_set.issubset(elf1_set):
			count += 1
	return count


def part2():
	count = 0
	for line in data:
		start, end = map(int, line[0].split('-'))
		elf1_set = {_ for _ in range(start, end+1)}
		start, end = map(int, line[1].split('-'))
		elf2_set = {_ for _ in range(start, end+1)}
		if elf1_set.intersection(elf2_set) != set():
			count += 1
	return count


if __name__ == "__main__":
	print("part 1: ", part1())
	print("part 2: ", part2())
