"""Day 01 Advent_of_Code 2023"""
with open("input/day01.txt", 'r') as infile:
	data = [line.rstrip() for line in infile]
look = {'1','2','3','4','5','6','7','8','9'}
translate = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


def fun(strings):
	number_Strings = []
	for line in strings:
		word = []
		for character in line:
			if character in look:
				word.append(character)
		number_Strings.append(word)
	sum_list = []
	for each in number_Strings:
		if each:
			temp_str = each[0] + each[-1]
			temp_int = int(temp_str)
			sum_list.append(temp_int)
	return sum(sum_list)


def part2(strings):
	number_Strings = []
	for line in strings:
		found = []
		for character in look:
			pointer = 0
			for _ in range(line.count(character)):
				found.append([line.find(character, pointer), character])
				pointer = line.find(character, pointer)+1
		for word in translate:
			if word in line:
				pointer = 0
				for _ in range(line.count(word)):
					found.append([line.find(word, pointer), translate[word]])
					pointer = line.find(word, pointer)+1
		found.sort()
		number_Strings.append(found)
	sum_list = []
	new_number_Strings = []
	for collection in number_Strings:
		new_string = ""
		for each in collection:
			new_string = new_string + each[1]
		new_number_Strings.append(new_string)
	for each in new_number_Strings:
		if each:
			temp_str = each[0] + each[-1]
			temp_int = int(temp_str)
			sum_list.append(temp_int)
	# for i, each in enumerate(data):
	# 	print(data[i])
	# 	print(sum_list[i])
	# 	throwaway = input()
	return sum(sum_list)


if __name__ == "__main__":
	print(fun(data))
	print(part2(data))
	# print("part 1: ")
	# print("part 2: ")
