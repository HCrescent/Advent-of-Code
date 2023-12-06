"""Day 06 Advent_of_Code 2023"""
from math import ceil
with open("input/day06.txt", 'r') as infile:
	data = [line.rstrip().split() for line in infile]
data[0].pop(0)
data[1].pop(0)


def product(values):
	"""Takes an iterable and creates a product of each element in the iterable

	:param values: List - (or other compatible iterable) to get the product of all elements
	:return: Int - Calculated product
	"""
	prod = 1
	for _ in values:
		prod *= _
	return prod


def fun(part2=False):
	if part2:
		data_copy = [[int(''.join(row))] for row in data]
	else:
		data_copy = [list(map(int, row)) for row in data]
	races = []
	for i, time in enumerate(data_copy[0]):
		candidates = 0
		for t in range(1, time+1):
			if ceil((data_copy[1][i]) / t) <= time - t:
				if (time-t) * t > data_copy[1][i]:
					candidates += 1
		races.append(candidates)
	return product(races)



if __name__ == "__main__":
	print("part 1: ", fun())
	print("part 2: ", fun(True))
