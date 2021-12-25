"""Day 01 Advent_of_Code 2015"""
with open("input/day01.txt", 'r') as infile:
	data = list(infile)
LEFT_PAR = data[0].count('(')
RIGHT_PAR = data[0].count(')')
floor = 0
for index, each in enumerate(data[0]):
	match each:
		case '(':
			floor += 1
		case ')':
			floor -= 1
	if floor == -1:
		break

if __name__ == "__main__":
	print("part 1: ", LEFT_PAR - RIGHT_PAR)
	print("part 2: ", index + 1)
