"""Day 10 Advent_of_Code 2023"""
with open("input/day10.txt", 'r') as infile:
	data = [line.rstrip() for line in infile]

move_dict = {'E': (0,1), 'SE': (1,1), 'S':(1,0), 'SW': (1,-1), 'W': (0,-1), 'NW': (-1,-1), 'N': (-1,0), 'NE': (-1,1)}
pipe_dict = {'|':('N', 'S'), '-':('E', 'W'), 'F':('E', 'S'), '7':('S', 'W'), 'J':('N', 'W'), 'L':('N', 'E'), '.':('0','0')}

class Pipe:
	def __init__(self, coordinate, steps):
		self.coord = tuple(coordinate)
		self.pipeType = data[coordinate[0]][coordinate[1]]
		self.connectors = pipe_dict[self.pipeType]
		self.steps = steps

	def __eq__(self, other):
		return self.coord == other.coord

	def __ne__(self, other):
		return self.coord != other.coord

	def __lt__(self, other):
		return self.steps < other.steps

	def __hash__(self):
		return hash(self.coord)

	def __repr__(self):
		return f"{self.pipeType}: {self.coord} steps: {self.steps}/"


def printPipes(coord):
	temp_p = []
	for each in data:
		temp_p.append(each)
	replacement = '\x1b[6;30;42m' + temp_p[coord[0]][coord[1]] + '\x1b[0m'
	temp_p[coord[0]] = temp_p[coord[0]][:coord[1]] + replacement + temp_p[coord[0]][coord[1]+1:]
	for _ in temp_p:
		print(_)
	print()
	return


def determineStart():
	start_location = None
	for i1, line in enumerate(data):
		for i2, character in enumerate(line):
			if character == 'S':
				start_location = (i1, i2)
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
	pipe = [k for k, v in pipe_dict.items() if v == tuple(pipe_entrances)]
	data[start_location[0]] = data[start_location[0]].replace('S', pipe[0])
	return start_location


def traverse(start_node):
	positive = {start_node}
	steps = 1
	current_node = Pipe([sum(_) for _ in zip(start_node.coord, move_dict[pipe_dict[start_node.pipeType][0]])], 1)
	positive.add(current_node)
	while True:
		for n in range(2):
			next_node = Pipe([sum(_) for _ in zip(current_node.coord, move_dict[current_node.connectors[n]])], steps+1)
			if not next_node in positive:
				current_node = next_node
				positive.add(current_node)
				steps+=1
				break
		else:
			return list(positive)


def part1():
	start_node = Pipe(determineStart(), 0)
	result = traverse(start_node)
	result.sort()
	return result[len(result)//2].steps


if __name__ == "__main__":
	print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
	print("part 1: ", part1())
	# print("part 2: ")
