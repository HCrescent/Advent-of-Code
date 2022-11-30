"""Day 06 Advent_of_Code 2015"""
with open("input/day06.txt", 'r') as infile:
	data = [[_[0], _[1].split(','), _[3].split(',')] for _ in [line.rstrip().rsplit(' ', 3) for line in infile]]
	data = [[each[0], tuple(int(x) for x in each[1]), tuple(int(x) for x in each[2])] for each in data]
light_grid = [[False for _ in range(1000)] for _ in range(1000)]  # create grid of off lights


def process_range(corner_1, corner_2, mode):
	"""

	:param corner_1: Tuple -
	:param corner_2:
	:param mode:
	:return:
	"""
	return


if __name__ == "__main__":
	for each in data:
		print(each)
	# print("part 1: ")
	# print("part 2: ")
