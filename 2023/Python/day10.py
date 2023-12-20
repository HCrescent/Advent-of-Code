"""Day 10 Advent_of_Code 2023"""
with open("input/day10.txt", 'r') as infile:
	data = [line.rstrip() for line in infile]

move_dict = {'E': (0,1), 'SE': (1,1), 'S':(1,0), 'SW': (1,-1), 'W': (0,-1), 'NW': (-1,-1), 'N': (-1,0), 'NE': (-1,1)}
pipe_dict = {'|':('N', 'S'), '-':('E', 'W'), 'F':('E', 'S'), '7':('S', 'W'), 'J':('N', 'W'), 'L':('N', 'E'), '.':('0','0')}

# plan now that pipe is hashable we will make a set of visited pipes (1 for each loop), we will do this once for S
# connector 1 full loop around pipe network then again in opposite direction for S connector 2 then we will line up
# the pipes by steps, and the spot where both steps are the same should be the farthest pipe segment (assuming the loop
# is properly odd to have a midpoint). While traversing the pipes, we will try both connectors and first one not in
# visited dicts we go, end clause is both connectors are in dict
class Pipe:
	def __init__(self, coordinate, steps):
		self.coord = tuple(coordinate)
		self.pipeType = coordinate[0][1]
		self.connectors = pipe_dict[self.pipeType]
		self.steps = steps+1

	def __eq__(self, other):
		return self.steps == other.steps

	def __lt__(self, other):
		return self.steps < other.steps

	def __hash__(self):
		return hash(self.coord)


def printPipes(coord):
	temp_p = []
	for each in data:
		temp_p.append(each)
	replacement = '\x1b[6;30;42m' + temp_p[coord[0]][coord[1]] + '\x1b[0m'
	temp_p[coord[0]] = temp_p[coord[0]][:coord[1]] + replacement + temp_p[coord[0]][coord[1]+1:]
	for _ in temp_p:
		print(_)
	return


def determineStart():
	start_location = None
	for i1, line in enumerate(data):
		for i2, character in enumerate(line):
			if character == 'S':
				start_location = (i1, i2)
				printPipes(start_location)
				break
		if start_location is not None:
			break
	pipe_entrances = []
	surroundings = [[sum(pair) for pair in zip(start_location, move_dict[_])] for _ in ['N','E','S','W']]
	# if north pipe has a south entrance, We know Starter pipe has a North entrance

	try:
		if pipe_dict[data[surroundings[0][0]][surroundings[0][1]]].count('S') == 1:
			pipe_entrances.append('N')
	except IndexError:
		pass
		# east pipe has west entrance
	try:
		if pipe_dict[data[surroundings[1][0]][surroundings[1][1]]].count('W') == 1:
			pipe_entrances.append('E')
	except IndexError:
		pass
		# south pipe has north entrance
	try:
		if pipe_dict[data[surroundings[2][0]][surroundings[2][1]]].count('N') == 1:
			pipe_entrances.append('S')
		# west pipe has
	except IndexError:
		pass
	try:
		if pipe_dict[data[surroundings[3][0]][surroundings[3][1]]].count('E') == 1:
			pipe_entrances.append('W')
	except IndexError:
		pass
	print(pipe_entrances)
	pipe = {k for k, v in pipe_dict.items() if v == tuple(pipe_entrances)}
	print(pipe)


def fun():
	pass


if __name__ == "__main__":
	determineStart()
	print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
	# print("part 1: ")
	# print("part 2: ")
