"""Day 05 Advent_of_Code 2022"""
with open("input/day05.txt", 'r') as infile:
	data = [line.rstrip() for line in infile]
split = data.index("")
movements = [[int(num[1]), num[3], num[5]] for num in [movement.split() for movement in data[split+1:]]]
stacks = {key: [] for key in data[split-1].split()}
boxes = data[:split-1]

for i, row in enumerate(boxes):
	row = row.replace("]    ", "] [0]").replace("    [", "[0] [").replace("     ", " [0] ").replace("   ", "[0]")
	while len(row) < (len(stacks)*4)-1:
		row = row + " [0]"
	boxes[i] = row
boxes = [each.split() for each in boxes]
for row in boxes[::-1]:
	for i, each in enumerate(row):
		if each != "[0]":
			stacks[str(i+1)].append(each[1])


def part1():
	for instruction in movements:
		for _ in range(instruction[0]):
			stacks[instruction[2]].append(stacks[instruction[1]].pop())
	top_string = [stacks[str(each+1)].pop() for each in range(len(stacks))]
	return "".join(top_string)



if __name__ == "__main__":
	print("part 1: ", part1())
	# print("part 2: ")
