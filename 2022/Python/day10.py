"""Day 10 Advent_of_Code 2022"""
with open("input/day10.txt", 'r') as infile:
	data = [line.rstrip().split(" ") for line in infile]
data = [[each[0], int(each[1])] if len(each) == 2 else [each[0]] for each in data]
display = [['.' for each in range(40)] for _ in range(6)]


def printDisplay():
	for each in display:
		print("".join(each))


def part1():
	cycles = [0]
	register = 1
	for instruction in data:
		cycles.append(register)
		if instruction[0] == "noop":
			pass
		if instruction[0] == "addx":
			cycles.append(register)
			register += instruction[1]
	for i in range(len(cycles)):
		cycles[i] = cycles[i] * i
	return sum(cycles[20:221:40])


def draw(cycle, reg):
	x, y, z = reg-1, reg, reg+1
	row = cycle // 40  # row of display
	position = (cycle - (row * 40))-1
	if position == x or position == y or position == z:
		display[row][position] = "#"
	return


def part2():
	cycles = [0]
	register = 1
	for instruction in data:
		cycles.append(register)
		draw(len(cycles)-1, register)
		if instruction[0] == "noop":
			pass
		if instruction[0] == "addx":
			cycles.append(register)
			draw(len(cycles)-1, register)
			register += instruction[1]
	return sum(cycles[20:221:40])


if __name__ == "__main__":
	print("part 1: ", part1())
	print("part 2: ")
	part2()
	printDisplay()
