"""Day 08 Advent_of_Code 2021"""
with open("input/day08.txt", 'r') as infile:
	data = list(infile)


def part1():
	data_p1 = []
	for each in data:
		data_p1.append(each[61:-1])
	data_p1 = [data_p1[_].split(' ') for _ in range(len(data_p1))]
	count = [0 for _ in range(8)]
	for each in data_p1:
		for sub in each:
			count[len(sub)] += 1
	return count[2] + count[3] + count[4] + count[7], data_p1


def part2(output_data):
	data_p2 = []
	for each in data:
		data_p2.append(each[:58])
	data_p2 = [data_p2[_].split(' ') for _ in range(len(data_p2))]
	print(data_p2)
	output_sum = 0
	for index, words in enumerate(data_p2):
		output_sum += solve(words, output_data[index])
	return output_sum


def solve(in_keys, out_keys):
	display_dict = {}
	for each in in_keys:
		if len(each) == 2:
			display_dict[each] = 1
		elif len(each) == 3:
			display_dict[each] = 7
		elif len(each) == 4:
			display_dict[each] = 4
		elif len(each) == 7:
			display_dict[each] = 8
	solve_three(in_keys, display_dict)
	print(display_dict)
	return 19


def solve_three(in_keys, display_dict):
	for each in in_keys:
		if len(each) == 5:
			for letter in (key for key, num in display_dict.copy().items() if num == 1):
				if letter[0] and letter[1] in each:
					display_dict[each] = 3
	pass


if __name__ == "__main__":
	part1, readings = part1()
	part2(readings)
	print("part 1: ", part1)
# print("part 2: ")
