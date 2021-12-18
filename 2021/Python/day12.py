"""Day 12 Advent_of_Code 2021"""
from collections import defaultdict
CAVES = defaultdict(list)
with open("input/day12.txt", 'r') as infile:
	data = [line.rstrip().split('-') for line in infile]
[data.append([each[1], each[0]]) for each in data[::-1]]  # append an inverse copy of cave paths
[CAVES[f"{each[0]}"].append(each[1]) for each in data]  # add all caves to a dict of available movements
UNIQUE_PATHS = {}


def recursive_cave(connected_caves, path_taken='', part2=False, flag=False):
	name = list(CAVES.keys())[list(CAVES.values()).index(connected_caves)]  # name of cave we are in
	path_taken += f"{name},"
	if name == "end":
		UNIQUE_PATHS[path_taken] = True  # update new unique path
		return  # return up one level of recursion to find more paths
	for each in connected_caves:
		if each == "start":
			continue
		new_flag = flag
		if each.islower() and f"{each}," in path_taken:  # if each is a small cave and already in our path
			if part2 and not new_flag:
				new_flag = True
			else:
				continue
		recursive_cave(CAVES[each], path_taken, part2, new_flag)
	return  # this should be our return when theres no options to move


if __name__ == "__main__":

	recursive_cave(CAVES["start"])
	print("part 1: ", len(UNIQUE_PATHS))
	recursive_cave(CAVES["start"], '', True)
	print("part 2: ", len(UNIQUE_PATHS))
