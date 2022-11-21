"""Day 05 Advent_of_Code 2015"""
with open("input/day05.txt", 'r') as infile:
	str_list = [line.rstrip() for line in infile]
alpha_set = list("abcdefghijklmnopqrstuvwxyz")
vowels_set = {'a', 'e', 'i', 'o', 'u'}
doubles_set = {char+char for char in alpha_set}
naughty_pairs = {"ab", "cd", "pq", "xy"}


def naughtyOrNice(string):
	# determine vowel count in string
	vowel_count = 0
	for char in string:
		if char in vowels_set:
			vowel_count += 1
	# if its less than three string is naughty
	if vowel_count < 3:
		return False
	# create list of adjacent letter pairs
	adjacents = [string[i]+string[i+1] for i in range(len(string)-1)]
	# determine string contains a double character
	for pair in adjacents:
		if pair in doubles_set:
			break
	else:  # no doubles found
		return False
	# check that no naughty pairs are in the string
	for pair in adjacents:
		if pair in naughty_pairs:
			return False
	else:  # we passed all 3 tests
		return True


if __name__ == "__main__":
	str_status = [naughtyOrNice(each) for each in str_list]
	print("part 1: ", str_status.count(True))
	# print("part 2: ")

