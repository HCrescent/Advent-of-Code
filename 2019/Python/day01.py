"""Day 01 Advent_of_Code 2019"""
with open("input/day01.txt", 'r') as infile:
	data = [int(line.rstrip()) for line in infile]


def fuel_cost(roster):
	running_sum = 0
	for each in roster:
		running_sum += each//3 - 2
	return running_sum

def fuel_calc(fuel):
	return  fuel//3 - 2

def fuel_cost_p2(roster):
	running_sum = 0
	for each in roster:
		while each > 0:
			each = fuel_calc(each)
			running_sum += each
		else:
			if each < 0:
				running_sum += -each

	return running_sum

if __name__ == "__main__":
	print("part 1: ", fuel_cost(data))
	print("part 2: ", fuel_cost_p2(data))
