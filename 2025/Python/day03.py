"""Day 03 Advent_of_Code 2025"""
with open("input/day03.txt", 'r') as infile:
	data = [line.rstrip() for line in infile]
data = [[int(digits) for digits in each] for each in data]
#
# def part1():
# 	total = 0
# 	for bank in data:
# 		tens = max(bank[:-1])
# 		position = bank.index(tens)+1
# 		ones = max(bank[position:])
# 		total += tens * 10 + ones
# 	return total
#

def part2(length):
	total = 0
	for bank in data:
		constructed_num = 0
		for n in range(length)[::-1]:
			lead = max(bank[:len(bank)-n])
			position = bank.index(lead)+1
			bank = bank[position:]
			constructed_num = constructed_num * 10 + lead
		total += constructed_num
	return total


if __name__ == "__main__":
	print("part 1: ", part2(2))
	print("part 2: ", part2(12))
