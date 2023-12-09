"""Day 09 Advent_of_Code 2023"""
with open("input/day09.txt", 'r') as infile:
	data = [list(map(int, line.rstrip().split())) for line in infile]


def buildDeltas(numbers):
	new_deltas = []
	for i in range(len(numbers)-1):
		new_deltas.append(numbers[i+1] - numbers[i])
	return new_deltas

def part1(deltas):
	if set(deltas) == {0}:
		return 0
	history_number = part1(buildDeltas(deltas))
	new_history_number = deltas[-1] + history_number
	return new_history_number


def part2(deltas):
	if set(deltas) == {0}:
		return 0
	history_number = part2(buildDeltas(deltas))
	new_history_number = deltas[0] - history_number
	return new_history_number


if __name__ == "__main__":
	part1sum = 0
	for each in data:
		part1sum += part1(each)
	print("part 1: ", part1sum)
	part2sum = 0
	for each in data:
		part2sum += part2(each)
	print("part 2: ", part2sum)
