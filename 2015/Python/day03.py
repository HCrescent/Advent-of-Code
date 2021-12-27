"""Day 03 Advent_of_Code 2015"""
with open("input/day03.txt", 'r') as infile:
	data = infile.read().rstrip()


def deliver(instructions):
	houses = {"(0,0)": 1}
	x = 0
	y = 0
	for each in instructions:
		match each:
			case '^':
				y += 1
			case '>':
				x += 1
			case 'v':
				y -= 1
			case '<':
				x -= 1
		if houses.get(f"({x},{y})") is None:
			houses[f"({x},{y})"] = 0
		# houses[f"({x},{y})"] += 1  # this line for knowing the number of presents delivered to each house
	return set(houses)


if __name__ == "__main__":
	print("part 1: ", len(deliver(data)))
	print("part 2: ", len(deliver(data[0::2]) | deliver(data[1::2])))
