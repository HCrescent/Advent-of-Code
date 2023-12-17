"""Day 08 Advent_of_Code 2023"""
import re
with open("input/day08.txt", 'r') as infile:
	data = [line.rstrip() for line in infile]

desert_dict = {}
moves = data[0]

class DesertNode:
	def __init__(self, line):
		self.data = line
		self.name = line.split(' = ')[0]
		self.children = {'L': line[7:10], 'R': line[12:15]}
		self.updateDict()

	def updateDict(self):
		desert_dict.update({self.name: self})

	def __hash__(self):
		return hash(self.name)

	def __repr__(self):
		return f"{self.data}"


def part1():
	for each in data[2:]:
		DesertNode(each)
	current_node = desert_dict['AAA']
	steps = 0
	move_cycle = len(moves)
	while current_node.name != 'ZZZ':
		current_node = desert_dict[current_node.children[moves[steps % move_cycle]]]
		steps += 1
	return steps


def part2():
	for each in data[2:]:
		DesertNode(each)
	current_nodes = [desert_dict[_] for _ in [key for key in desert_dict.keys() if re.match("..A", key)]]
	answer_nodes = []
	steps = 0
	move_cycle = len(moves)
	while len(answer_nodes) != len(current_nodes):
		for i, node in enumerate(current_nodes):
			current_nodes[i] = desert_dict[node.children[moves[steps % move_cycle]]]
		answer_nodes = [each.name for each in current_nodes if re.match("..Z", each.name)]
		steps += 1
		if steps % 10_000_000 == 0:
			print(steps)
	return steps



if __name__ == "__main__":
	# print("part 1: ", part1())
	print("part 2: ", part2())
