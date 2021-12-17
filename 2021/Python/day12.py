"""Day 12 Advent_of_Code 2021"""
from collections import defaultdict
CAVES = defaultdict(list)
with open("input/day12.txt", 'r') as infile:
	data = [line.rstrip().split('-') for line in infile]
[data.append([each[1], each[0]]) for each in data[::-1]]  # append an inverse copy of cave paths
[CAVES[f"{each[0]}"].append(each[1]) for each in data]  # add all caves to a dict of available movements
UNIQUE_PATHS = {}


def all_paths():
	count = 0

	pass


def recursive_cave(connected_caves, path_taken, record):
	end = []
	for each in connected_caves:
		if record.get(each, 1):  # if each is in our record of visited caves -> False, if not -> True
			if each == each.lower():
				record[each] = False
			path_taken += f"{each},"
			path_taken = recursive_cave(CAVES[each], path_taken, record)
			print(path_taken)
	return path_taken  # this should be our return when theres no options to move


if __name__ == "__main__":
	recursive_cave(CAVES["start"], ",start,", {'start': False})
# print("part 1: ")
# print("part 2: ")
