"""Day 03 Advent_of_Code 2025"""
with open("input/day03.txt", 'r') as infile:
	data = [line.rstrip() for line in infile]
data = [[int(digits) for digits in each] for each in data]

def part1():
	total = 0
	for bank in data:
		tens = max(bank[:-1])
		position = bank.index(tens)+1
		ones = max(bank[position:])
		total += tens * 10 + ones
	return total


def part2(length):
	N = length - 1
	total = 0
	for bank in data:
		lead = max(bank[:-N])
		position = bank.index(lead)
		bank = bank[position:]
		while len(bank) > length:
			bobby_tables = min(bank)
			bank.remove(bobby_tables)
		constructed_number = 0
		for each in bank:
			constructed_number = constructed_number * 10 + each
		total += constructed_number
	return total


if __name__ == "__main__":
	print("part 1: ", part1())
	print("part 2: ", part2(12))
