"""Day 06 Advent_of_Code 2025"""
from math import prod
with open("input/day06.txt", 'r') as infile:
	data = [line.rstrip().split() for line in infile]
operations = data[-1]
data1 = [list(map(int, each)) for each in data[:-1]]
data2 = []
#seperate sections by 4 vertical blanks, then process the strings vertically till you have integers and ready


def part1():
	total = 0
	for n in range(len(data1[0])):
		if operations[n] == '+':
			total += sum([data1[row][n] for row in range(len(data1))])
		else:
			total += prod([data1[row][n] for row in range(len(data1))])
	return total


if __name__ == "__main__":

	print("part 1: ", part1())
	print("part 2: ")
