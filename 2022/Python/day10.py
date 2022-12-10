"""Day 10 Advent_of_Code 2022"""
with open("input/day10.txt", 'r') as infile:
	data = [line.rstrip().split(" ") for line in infile]
data = [[each[0], int(each[1])] if len(each) == 2 else [each[0]] for each in data]
display = [['.' for each in range(40)] for _ in range(6)]


def printDisplay():
	for each in display:
		print("".join(each))


def draw(cycle, reg):
	""" Draw the screen, lit pixel if the register is within range of the currently active scanline

	:param cycle: Int - cycle count
	:param reg: Int - value in the register at this cycle
	:return: None
	"""
	# cycle = cycle % 240  # you would need this line if we were gonna draw more than one screen
	x, y, z = reg-1, reg, reg+1
	row = cycle // 40  # row of display
	position = (cycle - (row * 40))-1  # get position in that row
	if position == x or position == y or position == z:
		display[row][position] = "#"
	return


def processCycles():
	""" process the two operations and cycle lengths, calling the draw function for each cycle

	:return: Int - sum of 20th, 60th, 100th, 140th, 180th, 220th cycles
	"""
	cycles = [0]
	register = 1
	for instruction in data:
		cycles.append(register)
		draw(len(cycles)-1, register)
		if instruction[0] == "addx":
			cycles.append(register)
			draw(len(cycles)-1, register)
			register += instruction[1]
	for i in range(len(cycles)):  # update the cycle values for cycle scores
		cycles[i] *= i
	return sum(cycles[20:221:40])


if __name__ == "__main__":
	print("part 1: ", processCycles())
	print("part 2: ")
	printDisplay()
