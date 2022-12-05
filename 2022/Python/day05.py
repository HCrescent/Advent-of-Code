"""Day 05 Advent_of_Code 2022"""
with open("input/day05.txt", 'r') as infile:
	data = [line.rstrip() for line in infile]
split = data.index("")  # grab the index for separating box configuration from instructions
# format the movement instructions part of data into just the 3 values we need in [int, key, key] form
movements = [[int(num[1]), num[3], num[5]] for num in [movement.split() for movement in data[split+1:]]]
stacks = {key: [] for key in data[split-1].split()}  # initialize our dict of stacks
boxes = data[:split-1]  # get a list of just the boxes section

# this section is formatting the boxes text field for entry into stacks
for i, row in enumerate(boxes):
	# I replaced the whitespaces with a stand in for a non-existent box
	boxes[i] = row.replace("]    ", "] [0]").replace("    [", "[0] [").replace("   ", "[0]")
# now we can easily split the boxes in a way that keeps them enumerated to their proper stack
boxes = [each.split() for each in boxes]
for row in boxes[::-1]:
	for i, each in enumerate(row):
		if each != "[0]":  # don't put in the fake boxes
			stacks[str(i+1)].append(each[1])
# create a deep copy, could also use deepcopy() from copy library
# I used the dict/list comprehension just because I like the practice
# and avoiding imports for small simple scripts
stacks2 = {key: [_ for _ in items] for key, items in stacks.items()}


def part1():
	for instruction in movements:
		# loop for each box in a stack we want to move
		for _ in range(instruction[0]):
			# pop the source stack, append the destination stack
			stacks[instruction[2]].append(stacks[instruction[1]].pop())
	# get the top box of each stack
	top_string = [stacks[str(each+1)].pop() for each in range(len(stacks))]
	return "".join(top_string)  # return the string


def part2():
	for instruction in movements:
		temp_stack = []  # in order to simulate keeping order we will just re-reverse the order
		# loop for each box in a stack we want to move
		for _ in range(instruction[0]):
			# pop source stack to the temp stack
			temp_stack.append(stacks2[instruction[1]].pop())
		# pop the temp stack, to provide the destination stack with the proper order of boxes
		while temp_stack:
			stacks2[instruction[2]].append(temp_stack.pop())
	# get the top box of each stack
	top_string = [stacks2[str(each+1)].pop() for each in range(len(stacks2))]
	return "".join(top_string)  # return the string


if __name__ == "__main__":
	print("part 1: ", part1())
	print("part 2: ", part2())
