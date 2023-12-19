"""Day 08 Advent_of_Code 2023"""
import re
from math import lcm
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
	starting = [desert_dict[_] for _ in [key for key in desert_dict.keys() if re.match("..A", key)]]
	end_nodes = [desert_dict[_] for _ in [key for key in desert_dict.keys() if re.match("..Z", key)]]
	move_cycle = len(moves)
	cycle_steps = []
	for NODE in starting:
		node_steps = []
		temp_node = NODE
		continuous_steps = 0
		for _ in range(2):
			loop_steps = 1
			temp_node = desert_dict[temp_node.children[moves[continuous_steps % move_cycle]]]
			continuous_steps += 1
			while temp_node not in end_nodes:
				temp_node = desert_dict[temp_node.children[moves[continuous_steps % move_cycle]]]
				continuous_steps += 1
				loop_steps += 1
			node_steps.append(loop_steps)
		else:
			cycle_steps.append(node_steps[1])
	return lcm(*cycle_steps)



if __name__ == "__main__":
	print("part 1: ", part1())
	print("part 2: ", part2())
