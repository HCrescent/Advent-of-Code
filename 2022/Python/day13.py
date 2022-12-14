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
			correct_list.append((i//2)+1)
	return sum(correct_list)


def part2():
	while True:
		for i in range(len(data)-1):
			if processTwoLists(data[i], data[i+1]):
				continue
			else:  # swap the two
				break
		else:  # list was fully sorted
			return
		data[i], data[i+1] = data[i+1], data[i]


def processTwoLists(left, right):
	for i, each in enumerate(right):  # enumerate right list to match with left
		try:
			if left[i] == each:  # no determination yet keep going
				continue  # next iteration
			return callme(left[i], each)  # test left element and right element
		except IndexError:  # if left[i] produces index error
			return True  # left list was shorter we reached the conclusion that we have correct order


def callme(left, right):
	match (left, right):  # match the type of comparison going on this time
		case (list(), list()):  # list vs list
			return processTwoLists(left, right)
		case (int(), list()) | (list(), int()):  # integer vs list  the problem case
			if isinstance(left, int):  # if left is the int
				left = [left]
			if isinstance(right, int):  # if right is the int
				right = [right]
			return callme(left, right)  # two lists called
		case (int(), int()):
			return left < right  # if true we are all done go back up and out


if __name__ == "__main__":
	print(part1())
	data.append([[2]])
	data.append([[6]])
	part2()
	for each in data:
		print(each)
	# print("part 1: ")
	# print("part 2: ")
