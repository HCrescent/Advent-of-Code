"""Day 14 Advent_of_Code 2021"""
with open("input/day14.txt", 'r') as infile:
	data = [line.rstrip() for line in infile]
INIT = list(data.pop(0))
RULES = {}
RULES_COUNTS = {}
TOTAL_COUNTS = {}
NEW_RULES = {}
PART2_INIT = ""
data.pop(0)
[RULES.update({_.split(' -> ')[0]: _.split(' -> ')[1]}) for _ in data]


def insert(polymer, insertion):
	global PART2_INIT
	temp_poly = list(polymer)
	[temp_poly.insert(i + 1, insertion.pop()) for i in list(range(len(insertion)))[::-1]]
	PART2_INIT = "".join(temp_poly)
	return PART2_INIT


def buffer(polymer):
	insertion = [RULES["".join(polymer[i:i+2])] for i in range(len(polymer)-1)]
	return insertion


def buffer2(polymer):
	for letter in set(polymer):
		TOTAL_COUNTS[letter] += polymer.count(letter)
	# insertion = [RULES["".join(polymer[i:i + 2])] for i in range(len(polymer) - 1)]
	for i in range(len(polymer) - 1):
		for each in RULES_COUNTS["".join(polymer[i:i + 2])].keys():
			TOTAL_COUNTS[each] += RULES_COUNTS["".join(polymer[i:i + 2])][each]
	return


def grow(steps, polymer):
	for _ in range(steps):
		insertion = buffer(polymer)
		polymer = insert(polymer, insertion)
	return polymer


def part1(steps, polymer):
	result_polymer = grow(steps, polymer)
	counts = [result_polymer.count(each) for each in set(result_polymer)]
	counts.sort()
	return counts[-1] - counts[0]


def update_rules(steps):
	for each in RULES.keys():
		NEW_RULES[each] = grow(steps, each)
	for each in NEW_RULES.keys():
		temp_str = NEW_RULES[each]
		temp_list = list(temp_str)
		temp_list.pop()
		temp_list.pop(0)
		RULES[each] = "".join(temp_list)
	return


def create_dict_counts():
	for each in RULES.keys():
		temp_count_dict = {}
		temp_list = set(RULES[each])
		for letter in temp_list:
			TOTAL_COUNTS[letter] = 0
			temp_count_dict[letter] = RULES[each].count(letter)
		RULES_COUNTS[each] = temp_count_dict
	return


def grow_with_number_counts(polymer):
	buffer2(polymer)
	temp_list = [TOTAL_COUNTS[each] for each in TOTAL_COUNTS.keys()]
	temp_list.sort()
	return temp_list[-1] - temp_list[0]


if __name__ == "__main__":
	update_rules(10)
	print("part 1: ", part1(1, INIT))
	update_rules(2)
	part1(1, INIT)  # creating the new initial state
	create_dict_counts()
	print("part 2: ", grow_with_number_counts(PART2_INIT))
