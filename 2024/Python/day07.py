"""Day 07 Advent_of_Code 2024"""
with open("input/day07.txt", 'r') as infile:
	data = [line.rstrip().split(':') for line in infile]
targets = [int(each.pop(0)) for each in data]
operands = [list(map(int, each[0].split())) for each in data]


def to_base(num, base):
	if num == 0:
		return "0"
	digits = "012"
	result = ""
	while num > 0:
		result = digits[num % base] + result
		num //= base
	return result


def add(a, b):
	return a + b


def mul(a, b):
	return a * b


# this function looks different from all the others because it comes from my personal library of
# functions I wrote for project euler problems in a different project with more formal commentating.
def concatNum(value_a, value_b):
	""" takes two integers and concatenates them, inputs are treated as integers not strings
	for example, (1, 0) returns 10, (0, 1) returns 1, (1, 00) returns 10 because 00 == 0

	:param value_a: Int - left integer
	:param value_b: Int - right integer
	:return: Int - both integers concatenated
	"""
	width = len(str(value_b))
	concat = value_a * 10**width + value_b
	return concat


def part1(total_operators):
	flags = [True for _ in targets]
	# for each case in our puzzle
	for i, goal in enumerate(targets):
		exponent = len(operands[i]) - 1
		#for each possible permutation of operators create a mask
		for num in range(total_operators**exponent):
			mask = to_base(num, total_operators).zfill(exponent)
			# process the operands
			last = operands[i][0]
			for index, each in enumerate(operands[i][1:]):
				match mask[index]:
					case '0':
						operator = add
					case '1':
						operator = mul
					case '2':
						operator = concatNum
					case _:
						print("shouldn't get here")
						exit(1)
				last = operator(last, each)
			if last == goal:
				break
		else: # no sequence of operators resulted in the goal
			flags[i] = False
	return sum([targets[i] for i, each in enumerate(flags) if each])


if __name__ == "__main__":
	print("part 1: ", part1(2))
	print("part 2: ", part1(3))
