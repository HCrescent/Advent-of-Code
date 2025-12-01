"""Day 01 Advent_of_Code 2025"""
with open("input/day01.txt", 'r') as infile:
	data = [[line[0], int(line[1::])] for line in infile]
dial = [n for n in range(0,100)]


def left(index):
	return dial[index-1]


def right(index):
	return dial[(index+1)%100]


def part1():
	index = 50
	total = 0
	for Turn in data:
		if Turn[0] == 'L':
			index = (index - Turn[1]) % 100
		else:
			index = (index + Turn[1]) % 100
		index = dial[index]
		if index == 0:
			total += 1
	return total


def part2():
	index = 50
	total = 0
	for Turn in data:
		if Turn[0] == 'L':
			for _ in range(Turn[1]):
				index = left(index)
				if index == 0:
					total += 1
		else:
			for _ in range(Turn[1]):
				index = right(index)
				if index == 0:
					total += 1
	return total


if __name__ == "__main__":
	print("part 1: ", part1())
	print("part 2: ", part2())
