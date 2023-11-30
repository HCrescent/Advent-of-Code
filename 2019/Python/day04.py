"""Day 04 Advent_of_Code 2019"""
with open("input/day04.txt", 'r') as infile:
	data = list(map(int, infile.read().rstrip().split('-')))


def pass1(cand_nums):
	candidate_list2 = []
	for number in cand_nums:
		width = len(str(number))
		test_digit = 0
		for magnitude in range(width)[::-1]:
			selected_digit = (number // 10 ** magnitude) % 10
			if selected_digit < test_digit:
				break
			test_digit = selected_digit
		else:
			candidate_list2.append(number)
	return candidate_list2


def pass2(cand_nums):
	candidate_list = []
	for number in cand_nums:
		if len(set(str(number))) < 6:
			candidate_list.append(number)
	return candidate_list


def pass3(cand_nums):
	candidate_list = []
	for number in cand_nums:  # for each live candidate
		testing_string = str(number)  # make it a string
		test_set = set(testing_string)  # find which numbers to count
		digit_counts = {}  # set up dict
		for each in test_set:  # for each digit to count
			digit_counts.update({int(each): testing_string.count(each)})  # add a dict entry of #: times
		# if any entry is exactly 2
		if list(digit_counts.values()).count(2) >= 1:
			candidate_list.append(number)
	return candidate_list


if __name__ == "__main__":
	scope = [each for each in range(data[0], data[1]+ 1)]
	candidates = pass1(scope)
	candidates2 = pass2(candidates)
	print("part 1: ", len(candidates2))
	print("part 2: ", len(pass3(candidates2)))
