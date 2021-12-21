"""Day 14 Advent_of_Code 2021"""
with open("input/day14.txt", 'r') as infile:
	data = [line.rstrip() for line in infile]
INIT = data.pop(0)
RULES = {}
data.pop(0)
[RULES.update({_.split(' -> ')[0]:_.split(' -> ')[1]}) for _ in data]
print(INIT)


def insert(polymer, insertion):
	temp_poly = list(polymer)
	[temp_poly.insert(i+1, insertion.pop()) for i in list(range(len(insertion)))[::-1]]
	new = "".join(temp_poly)
	print(new)
	return new


def buffer(polymer):
	insertion = [RULES[polymer[i:i+2]] for i in range(len(polymer)-1)]
	return insertion


def grow(steps, polymer=INIT):
	for _ in range(steps):
		insertion = buffer(polymer)
		polymer = insert(polymer, insertion)
	return polymer


def part1(steps):
	result_polymer = grow(steps)
	counts = [result_polymer.count(each) for each in set(result_polymer)]
	counts.sort()
	return counts[-1] - counts[0]


if __name__ == "__main__":
	print("part 1: ", part1(10))
	print("part 2: ")
