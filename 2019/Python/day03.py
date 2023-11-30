"""Day 03 Advent_of_Code 2019"""
with open("input/day03.txt", 'r') as infile:
	data = [[[move[:1], int(move[1:])] for move in wire] for wire in [line.rstrip().split(',') for line in infile]]

move_dict = {'R': [1, 0], 'D': [0, -1], 'L': [-1, 0], 'U': [0, 1]}


def manhattan_distance(coordinate1, coordinate2):
	return abs(coordinate1[0] - coordinate2[0]) + abs(coordinate1[1] - coordinate2[1])


def build_wires(part2 = False):
	origin = [0, 0]
	wire1 = [0, 0]
	wire2 = [0, 0]
	wire1_set = set()
	wire2_set = set()
	for move in data[0]:
		for _ in range(move[1]):
			# add the movement to the current coordinate and add the coord to the set of moved places
			wire1 = [sum(coordinate) for coordinate in zip(wire1, move_dict[move[0]])]
			wire1_set.add(tuple(wire1))
	for move in data[1]:
		for _ in range(move[1]):
			# add the movement to the current coordinate and add the coord to the set of moved places
			wire2 = [sum(coordinate) for coordinate in zip(wire2, move_dict[move[0]])]
			wire2_set.add(tuple(wire2))
	# intersection set will be all shared wire locations
	intersections = wire1_set.intersection(wire2_set)
	manhattans = [manhattan_distance(origin, list(each)) for each in intersections]

	if part2:
		steps1 = 0
		steps2 = 0
		wire1 = [0, 0]
		wire2 = [0, 0]
		wire1_steps = {}
		wire2_steps = {}
		for move in data[0]:
			for _ in range(move[1]):
				# add the movement to the current coordinate
				wire1 = [sum(coordinate) for coordinate in zip(wire1, move_dict[move[0]])]
				steps1 += 1
				# if the current step is in the intersections set from part 1, add that step count and intersection
				# to a dictionary
				if len({tuple(wire1)}.intersection(intersections)) > 0:
					wire1_steps.update({tuple(wire1): steps1})

		for move in data[1]:
			for _ in range(move[1]):
				# add the movement to the current coordinate
				wire2 = [sum(coordinate) for coordinate in zip(wire2, move_dict[move[0]])]
				steps2 += 1
				# if the current step is in the intersections set from part 1, add that step count and intersection
				# to a dictionary
				if len({tuple(wire2)}.intersection(intersections)) > 0:
					wire2_steps.update({tuple(wire2): steps2})

		crosses = wire1_steps.keys() & wire2_steps.keys()
		solution_dict = {}
		for key in crosses:
			solution_dict.update({key: wire1_steps[key] + wire2_steps[key]})
		return min(solution_dict.values())
	return min(manhattans)


if __name__ == "__main__":
	print("part 1: ", build_wires())
	print("part 2: ", build_wires(True))
