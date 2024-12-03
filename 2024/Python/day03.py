"""Day 03 Advent_of_Code 2024"""
import re
with open("input/day03.txt", 'r') as infile:
	data = [line.rstrip() for line in infile]
	data = "".join(data)

def mul(a, b):
	return a * b


def part1():
	filtered = re.findall("mul\(\d?\d?\d?,\d?\d?\d?\)", data)
	total = 0
	for each in filtered:
		total += eval(each)
	return total


if __name__ == "__main__":
	print("part 1: ", part1())
	part2filter = re.split("don't\(\).*?do\(\)", data)
	data = "".join(part2filter)
	print("part 2: ", part1())
