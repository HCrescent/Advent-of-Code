"""Day 02 Advent_of_Code 2025"""
from math import log10
with open("input/day02.txt", 'r') as infile:
	data = [line.rstrip().split(',') for line in infile]
data = [list(map(int, pair.split('-'))) for each in data for pair in each]


def validator_p1(number):
	valid = True
	# if the number has an even number of digits, check for two halves equaling each other, if it does flag false
	if (log10(number).__floor__()+1) % 2 == 0:
		n_string = str(number)
		midpoint = len(n_string)//2
		pair_a, pair_b = n_string[:midpoint], n_string[midpoint:]
		if pair_a == pair_b:
			valid = False
	return valid


def validator_p2(number):
	valid = True
	n_string = str(number)
	number_width = len(n_string)
	whole_divisors = []
	for n in range(1, number_width+1):
		if number_width % n == 0:
			whole_divisors.append(n)
	for period in whole_divisors[:-1]:
		segments = []
		index = 0
		while index < number_width:
			segments.append(n_string[index:index+period])
			index += period
		if len(set(segments)) == 1:
			valid = False
			break
	return valid


def part1():
	total = 0
	for start, end in data:
		for n in range(start, end+1):
			if not validator_p1(n):
				total +=n
	return total


def part2():
	total = 0
	for start, end in data:
		for n in range(start, end + 1):
			if not validator_p2(n):
				total += n
	return total


if __name__ == "__main__":
	print("part 1: ", part1())
	print("part 2: ", part2())
