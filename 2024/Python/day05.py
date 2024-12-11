"""Day 05 Advent_of_Code 2024"""
with open("input/day05.txt", 'r') as infile:
	data = infile.read()
rules, data = data.split("\n\n")
rules = rules.split('\n')
data = data.rstrip().split('\n')
rules = [list(map(int, each.split('|'))) for each in rules]
data = [[int(each) for each in test.split(',')] for test in data]


def relevant_rules(unknown_ordering: list) -> list:
	rules_to_use = []
	test_set = set(unknown_ordering)
	for pair in rules:
		if set(pair).issubset(test_set):
			rules_to_use.append(pair)
	return rules_to_use


def test_correctness(test_order: list) -> bool:
	result = False
	for rule in relevant_rules(test_order):
		if test_order.index(rule[0]) > test_order.index(rule[1]):
			break
	else:
		result = True
	return result


def part1() -> int:
	total = 0
	for each in data:
		if test_correctness(each):
			total += each[len(each)//2]
	return total


def part2():
	total = 0
	for test_case in data:
		rule_list = relevant_rules(test_case)
		if not test_correctness(test_case):
			rankings = []
			occurrences = [rule[0] for rule in rule_list]
			for number in test_case:
				rankings.append([occurrences.count(number), number])
			rankings.sort()
			total += rankings[len(rankings)//2][1]
	return total


if __name__ == "__main__":
	print("part 1: ", part1())
	print("part 2: ", part2())
