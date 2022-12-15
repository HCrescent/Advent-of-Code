"""Day 13 Advent_of_Code 2022"""
from ast import literal_eval  # the safer eval() function BE SAFE
with open("input/day13.txt", 'r') as infile:
	data = infile.read().split("\n\n")
data = [each.rstrip().split("\n") for each in data]  # get rest of line breaks
data = [each for sublist in data for each in sublist]  # flatten
data = [literal_eval(each) for each in data]  # eval


def part1():
	correct_list = []
	for i in range(len(data)-1)[::2]:
		if processTwoLists(data[i], data[i+1]):
			correct_list.append((i//2)+1)  # index by pair
	return sum(correct_list)


# noinspection PyTypeChecker
def part2():
	# inefficient sorting
	while True:
		for i in range(len(data)-1):
			if data[i] != data[i+1]:  # don't bother with equivalent packets
				if processTwoLists(data[i], data[i+1]):
					continue
				else:  # swap the two
					break
		else:  # list was fully sorted
			divider1_i = data.index(divider1)+1
			divider2_i = data.index(divider2)+1
			return divider1_i * divider2_i
		data[i], data[i+1] = data[i+1], data[i]  # swap


def processTwoLists(left_list, right_list):
	for i, each in enumerate(right_list):  # enumerate right list to match with left
		try:
			if left_list[i] == each:  # no determination yet keep going
				continue
			test = testLR(left_list[i], each)  # test left element and right element if they are different
			if test is None:  # catches int, list being equivalent AFTER conversion
				continue
			return test
		except IndexError:  # if left[i] produces index error
			return True  # left list was shorter we reached the conclusion that we have correct order
	else:  # we finished through the list, if they are equivalent we return None
		if len(right_list) < len(left_list):
			return False  # list out of order


def testLR(left, right):
	match (left, right):  # match the type of comparison going on this time
		case (list(), list()):  # list vs list
			return processTwoLists(left, right)
		case (int(), list()) | (list(), int()):  # integer vs list
			if isinstance(left, int):  # if left is the int
				left = [left]
			if isinstance(right, int):  # if right is the int
				right = [right]
			return processTwoLists(left, right)  # two lists called
		case (int(), int()):
			return left < right  # if true we are all done go back up and out


if __name__ == "__main__":
	print("part 1: ", part1())
	divider1 = [[2]]
	divider2 = [[6]]
	data.append(divider1)
	data.append(divider2)
	print("part 2: ", part2())
