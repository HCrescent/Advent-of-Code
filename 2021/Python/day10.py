"""Day 10 Advent_of_Code 2021"""
with open("input/day10.txt", 'r') as infile:
	matrix_map = [list(line) for line in infile]
OPEN_CHARS = {'(': ')', '[': ']', '{': '}', '<': '>'}
ERROR_POINTS = {')': 3, ']': 57, '}': 1197, '>': 25137}
AUTO_POINTS = {')': 1, ']': 2, '}': 3, '>': 4}


def score(data_list):
	error_score = 0
	auto_score = []
	for each in data_list:
		error, auto = parse(each)
		error_score += error
		if auto > 0:
			auto_score.append(auto)
	auto_score.sort()
	return error_score, auto_score[len(auto_score)//2]


def parse(syntax):
	stack = []
	while syntax[0] != '\n':
		if syntax[0] in OPEN_CHARS:
			stack.append(syntax.pop(0))
		else:
			if OPEN_CHARS[stack[-1]] == syntax[0]:
				# pop properly paired chars
				stack.pop()
				syntax.pop(0)
			else:
				# found our unexpected closing char
				return ERROR_POINTS[syntax[0]], 0
	# clear newline char to start autocomplete
	syntax.pop()
	auto_score = 0
	while len(stack) > 0:
		syntax.append(OPEN_CHARS[stack.pop()])
		auto_score *= 5
		auto_score += AUTO_POINTS[syntax[-1]]
	return 0, auto_score


if __name__ == "__main__":
	part1, part2 = score(matrix_map)
	print("part 1: ", part1)
	print("part 2: ", part2)
