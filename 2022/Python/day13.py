"""Day 13 Advent_of_Code 2022"""
import sys
from ast import literal_eval  # the safer eval() function BE SAFE
with open("input/day13.txt", 'r') as infile:
	data = infile.read().split("\n\n")
data = [each.rstrip().split("\n") for each in data]
data = [each for sublist in data for each in sublist]


def fun():
	correct_list = []
	for i in range(len(data)-1)[::2]:
		argument1 = literal_eval(data[i])
		argument2 = literal_eval(data[i+1])
		if callme(argument1, argument2):
			correct_list.append((i//2)+1)
	return sum(correct_list)


def fun2():
	for i, pair in enumerate(data):
		argument1 = literal_eval(pair[0])
		argument2 = literal_eval(pair[1])
		if callme(argument1, argument2):
			continue
		else:
			break
	return


def callme(left, right):
	match (left, right):  # match the type of comparison going on this time
		case (list(), list()):  # list vs list
			for i, each in enumerate(right):  # enumerate right list to match with left
				try:
					if callme(left[i], each):  # test left element and right element
						return True  # we found an positive ordering condition
					elif left[i] == each:  # no determination yet keep going
						continue  # next iteration
					else:  # right integer was larger than left integer
						return False
				except IndexError:  # if left[i] produces index error
					return True  # left list was shorter we reached the conclusion that we have correct order
			else:  # right list empty before left list
				return False
		case (int(), list()) | (list(), int()):  # integer vs list  the problem case
			if isinstance(left, int):  # if left is the int
				left = [left]
			if isinstance(right, int):  # if right is the int
				right = [right]
			if callme(left, right):
				return True
			else:
				return False
		case (int(), int()):
			return left < right  # if true we are all done go back up and out


if __name__ == "__main__":
	print(fun())
	# print("part 1: ")
	# print("part 2: ")
