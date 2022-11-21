"""Day 05 Advent_of_Code 2015"""
with open("input/day05.txt", 'r') as infile:
	str_list = [line.rstrip() for line in infile]
alpha_list = list("abcdefghijklmnopqrstuvwxyz")
vowels_set = {'a', 'e', 'i', 'o', 'u'}
doubles_set = {char+char for char in alpha_list}
naughty_pairs = {"ab", "cd", "pq", "xy"}


def naughtyOrNicePart1(string):
	"""With a set of predetermined rules, evaluates a string as True if Nice, False if Naughty.

	:param string: Str - string of letters to analyze
	:return: Bool - False if Naughty, True if Nice
	"""
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


def naughtyOrNicePart2(string):
	"""With a set of predetermined rules, evaluates a string as True if Nice, False if Naughty.

	:param string: Str - string of letters to analyze
	:return: Bool - False if Naughty, True if Nice
	"""
	adjacents = [string[i] + string[i+1] for i in range(len(string)-1)]
	# determine if there are non-overlapping repeat pairs of letters
	for pair in adjacents:
		if string.count(pair) > 1:
			break
	else:  # didn't break so string is Naughty
		return False
	# determine if there is a repeating character with any single char between them
	for i in range(len(string)-2):
		if string[i] == string[i+2]:
			return True  # passed both criteria, string is NICE
	else:  # still here? we didn't find anything second criteria, string is NAUGHTY
		return False


if __name__ == "__main__":
	str_status = [naughtyOrNicePart1(each) for each in str_list]
	print("part 1: ", str_status.count(True))
	str_status = [naughtyOrNicePart2(each) for each in str_list]
	print("part 2: ", str_status.count(True))
