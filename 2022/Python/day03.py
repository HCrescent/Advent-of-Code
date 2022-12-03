"""Day 03 Advent_of_Code 2022"""
with open("input/day03.txt", 'r') as infile:
	data2 = [line.rstrip() for line in infile]
data = [[line[:(len(line)//2)], line[(len(line)//2):]] for line in data2]
alpha = "abcdefghijklmnopqrstuvwxyz"
lower = {each: n+1 for n, each in enumerate(alpha)}
upper = {each: n+27 for n, each in enumerate(alpha.upper())}
scores = lower | upper


def part1():
	priority_sum = 0
	for pack in data:
		for each in pack[0]:
			if each in pack[1]:
				priority_sum += scores[each]
				break
	return priority_sum


def part2():
	priority_sum = 0
	while data2:
		set0 = {x for x in data2.pop()}
		set1 = {x for x in data2.pop()}
		set2 = {x for x in data2.pop()}
		letter = set0.intersection(set1, set2)
		priority_sum += scores[letter.pop()]
	return priority_sum


if __name__ == "__main__":
	print("part 1: ", part1())
	print("part 2: ", part2())
