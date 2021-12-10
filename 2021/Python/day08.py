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
	output_sum = 0
	for index, words in enumerate(data_p2):
		output_sum += solve(words, output_data[index])
	return output_sum


def solve(in_words, out_words):
	setlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	# first pass will always get 4 unique digits
	for each in in_words:
		if len(each) == 2:
			setlist[1] = each
			one = set(each)
		elif len(each) == 3:
			setlist[7] = each
		elif len(each) == 4:
			setlist[4] = each
			four = set(each)
		elif len(each) == 7:
			setlist[8] = each
	# second pass gets all digits except 5 and 2
	for each in in_words:
		if each not in setlist:  # skip known keys
			if len(each) == 5:
				if one < set(each):
					setlist[3] = each
			elif len(each) == 6:
				if four < set(each):
					setlist[9] = each
				elif one < set(each):
					setlist[0] = each
				else:
					setlist[6] = each
					six = set(each)
					final_piece = one - six  # final_piece is the set element to determine 5 and 2
	# third pass tests and assigns 5 and 2 against our final_piece
	for each in in_words:
		if each not in setlist:  # skip known keys
			if len(each) == 5:
				if final_piece < set(each):
					setlist[2] = each
				else:
					setlist[5] = each
	decoded_number = ""
	for code in out_words:
		for i, word in enumerate(setlist):
			if set(code) == set(word):
				decoded_number += str(i)
	return int(decoded_number)


if __name__ == "__main__":
	part1, readings = part1()
	print("part 1: ", part1)
	print("part 2: ", part2(readings))
