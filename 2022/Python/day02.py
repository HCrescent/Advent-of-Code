"""Day 02 Advent_of_Code 2022"""
with open("input/day02.txt", 'r') as infile:
	data = [line.rstrip().split() for line in infile]

scores = {'X': 1, 'Y': 2, 'Z': 3}
lose = {'A': 'Z', 'B': 'X', 'C': 'Y'}
win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}


def part1(rounds):
	score = 0
	for each in rounds:
		match each:
			case ['A', 'Y']:
				score += 8
			case ['A', 'Z']:
				score += scores[each[1]]
			case ['B', 'X']:
				score += scores[each[1]]
			case ['B', 'Z']:
				score += 9
			case ['C', 'X']:
				score += 7
			case ['C', 'Y']:
				score += scores[each[1]]
			case _:
				score = score + 3 + scores[each[1]]
	return score


def part2(rounds):
	score = 0
	for each in rounds:
		match each[1]:
			case 'X':
				score += scores[lose[each[0]]]
			case 'Y':
				score += 3 + scores[draw[each[0]]]
			case 'Z':
				score += 6 + scores[win[each[0]]]
	return score


if __name__ == "__main__":
	print("part 1: ", part1(data))
	print("part 2: ", part2(data))
