"""Day 13 Advent_of_Code 2022"""
from ast import literal_eval  # the safer eval() function BE SAFE
with open("input/day13.txt", 'r') as infile:
	data = infile.read().split("\n\n")
data = [each.rstrip().split("\n") for each in data]


def fun():
	correct_list = []
	for i, pair in enumerate(data):
		argument1 = literal_eval(pair[0])
		argument2 = literal_eval(pair[1])
		if callme(argument1, argument2):
			correct_list.append(i+1)
	print(correct_list)
	return sum(correct_list)


def fun2():
	while True:
		for i in range(len(data)-1):
			argument1 = literal_eval(data[i])
			argument2 = literal_eval(data[i+1])
			if i == 11:
				print("here")
			if callme(argument1, argument2):
				continue
			else:  # swap the two
				break
		else:  # list was fully sorted
			return
		data[i], data[i+1] = data[i+1], data[i]


def callme(left, right):
	# print(left)
	# print(right)
	# print()
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
				try:
					left = [left]
					# in this case for the two lists left and right, left[0] < right[0] inputs in correct order:
					# if they are equal left side empyts first resulting true, if right is smaller, wrong order
					# thus test condition right smaller than left, True, else false
					print(len(right))
					if right[0] < left[0]:
						return False
					else:
						return True
				except TypeError:
					all_variables = dir()
					for name in all_variables:
						if not name.startswith('__'):
							my_value = eval(name)
							print(name, "is", type(my_value), "and is equal to ", my_value)
					raise IndexError
			if isinstance(right, int):  # if right is the int
				right = [right]
				# in this case, for two lists left and right, left[0] < right[0], everything is correct order
				# if they are equal or right[0] < left[0], then right list runs out first thus being out of order
				if left[0] < right[0]:
					return True
				else:
					return False
		case (int(), int()):
			return left < right  # if true we are all done go back up and out


if __name__ == "__main__":
	print(fun())
	data = [each for sublist in data for each in sublist]
	fun2()
	print(data)
	# print("part 1: ")
	# print("part 2: ")
