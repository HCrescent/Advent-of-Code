"""Day 11 Advent_of_Code 2022"""
with open("input/day11.txt", 'r') as infile:
	data = [line.rstrip().split() for line in infile]
# for every 7th line from the first objects line, int the first 2 chars of the strings in sliced line[2:]
starting_lists = [[int(num[:2]) for num in line[2:]] for line in data[1::7]]  # list of each starting monkeys items
monkeys = {i: starting_lists[i] for i, _ in enumerate(data[::7])}  # monkey dictionary {id: monkey items}
test_modulus = [int(line[-1]) for line in data[3::7]]  # give a list of the tests for each monkey
operation_lines = [line[-3:] for line in data[2::7]]  # get info for each monkeys operation
true_destinations = [int(line[-1]) for line in data[4::7]]  # addresses for modulus true
false_destinations = [int(line[-1]) for line in data[5::7]]  # addresses for modulus false
operator_lambdas = {
	"+": lambda a, b: a+b,
	"-": lambda a, b: a-b,
	"*": lambda a, b: a*b,
}


def runMonkeys(rounds):
	inspection_counts = [0 for _ in range(len(monkeys))]  # inspection totals for each monkey
	for _ in range(rounds):  # for number of rounds
		for i in range(len(monkeys)):  # for each monkey
			for inspection in monkeys[i]:  # for each object the monkey has
				inspection_counts[i] += 1  # increase that monkeys inspection tracker
				if operation_lines[i][0] == "old":  # if left input is supposed to be current object
					left = inspection
				else:  # else left input provides an integer literal
					left = int(operation_lines[i][0])
				if operation_lines[i][-1] == "old":  # if right input is supposed to be current object
					right = inspection
				else:  # else right input provides an integer literal
					right = int(operation_lines[i][-1])
				new = operator_lambdas[operation_lines[i][1]](left, right) // 3 # call the correct lambda based on str key
				if new % test_modulus[i]:  # true if remainder, False if no remainder
					monkeys[false_destinations[i]].append(new)  # append the new number to the destination monkey's list
				else:
					monkeys[true_destinations[i]].append(new)  # append the new number to the destinations monkey's list
			monkeys[i].clear()
		# for _ in range(len(monkeys)):
		# 	print(_, monkeys[_])
		# print()
	return inspection_counts


if __name__ == "__main__":
	inspection_totals = runMonkeys(20)
	inspection_totals.sort()
	monkey_business = inspection_totals[-2] * inspection_totals[-1]
	print("part 1: ", monkey_business)
	# print("part 2: ")
	pass
