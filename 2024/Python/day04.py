"""Day 04 Advent_of_Code 2024"""
with open("input/day04.txt", 'r') as infile:
	data = ["..." + line.rstrip() + "..." for line in infile]

filler = "".rjust(len(data[0]), ".")
for _ in range(3):
	data.insert(0, filler)
	data.insert(len(data), filler)


def bullseye(row, column):
	hits = 0
	# ↑
	word0 = "".join(["X", data[row-1][column], data[row-2][column], data[row-3][column]])
	# ↗
	word1 = "".join(["X", data[row-1][column+1], data[row-2][column+2], data[row-3][column+3]])
	# →
	word2 = "".join(["X", data[row][column+1], data[row][column+2], data[row][column+3]])
	# ↘
	word3 = "".join(["X", data[row+1][column+1], data[row+2][column+2], data[row+3][column+3]])
	# ↓
	word4 = "".join(["X", data[row+1][column], data[row+2][column], data[row+3][column]])
	# ↙
	word5 = "".join(["X", data[row+1][column-1], data[row+2][column-2], data[row+3][column-3]])
	# ←
	word6 = "".join(["X", data[row][column-1], data[row][column-2], data[row][column-3]])
	# ↖
	word7 = "".join(["X", data[row-1][column-1], data[row-2][column-2], data[row-3][column-3]])
	group = [word0, word1, word2, word3, word4, word5, word6, word7]
	for word in group:
		if word == "XMAS":
			hits += 1
	return hits


def masCross(row, column):
	solution_set = {"MMSS", "SSMM", "SMSM", "MSMS"}
	test_string = "".join([data[row-1][column-1], data[row-1][column+1], data[row+1][column-1], data[row+1][column+1]])
	if test_string in solution_set:
		return True


def part1():
	total = 0
	for Y, row in enumerate(data):
		for X, column in enumerate(row):
			if column == "X":
				total += bullseye(Y, X)
	return total


def part2():
	total = 0
	for Y, row in enumerate(data):
		for X, column in enumerate(row):
			if column == "A":
				if masCross(Y, X):
					total += 1
	return total


if __name__ == "__main__":
	print("part 1: ", part1())
	print("part 2: ", part2())
