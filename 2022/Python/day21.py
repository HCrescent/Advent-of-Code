"""Day 21 Advent_of_Code 2022"""
with open("input/day21.txt", 'r') as infile:
	data = [[each[0][:4], each[1:]] for each in [line.rstrip().split() for line in infile]]
monkey_literals = {each[0]: int(each[1][0]) for each in data if each[1][0].isnumeric()}
monkey_jobs = {each[0]: each[1] for each in data if len(each[1]) > 1}
operator_lambdas = {
	"+": lambda a, b: a+b,
	"*": lambda a, b: a*b,
	"-": lambda a, b: a-b,
	"/": lambda a, b: a/b,
}


def evaluate_job(instruction):
	""" takes a monkey expression and through recursion evaluates all dependencies ultimately solving the expression

	:param instruction: List - monkey job expression
	:return: Int/float - the result of the instruction expression
	"""
	operand_1 = instruction[0]
	operand_2 = instruction[2]
	if operand_1 in monkey_jobs:
		literal_1 = evaluate_job(monkey_jobs[operand_1])
	else:
		literal_1 = monkey_literals[operand_1]
	if operand_2 in monkey_jobs:
		literal_2 = evaluate_job(monkey_jobs[operand_2])
	else:
		literal_2 = monkey_literals[operand_2]
	return operator_lambdas[instruction[1]](literal_1, literal_2)  # evaluate expression based on operator char


def findSeed():
	""" The output of our input at humn = 0 is much larger than the right operand, and decreases
	linearly as humn increases, we can hone in on the correct seed by checking orders of magnitude until we overshoot

	:return: Int - the seed required to make root equality true
	"""
	# the problem wants us to find equality, but since we are honing in closer and closer to the value we want
	# a comparison that will give us information about the relation of the two numbers rather than equality
	operator_lambdas.update({"=": lambda a, b: a <= b})
	m = 0  # initialize magnitude
	flag = True
	# build magnitude up until we find the upper bound bound overshoot
	while flag:
		i = 10**m  # initialize starting value to current smallest order of magnitude
		for _ in range(9):  # check each quantity in the current order of magnitude (minus 1 for initialization)
			monkey_literals['humn'] = i
			if evaluate_job(monkey_jobs['root']):
				starting_number = i - 10**m  # i is an overshoot, so we undo the last addition
				flag = False
				break
			i += 10**m
		else:  # didn't break increase magnitude
			m += 1
	# approach seed one order of magnitude at a time
	for m in range(m)[::-1]:
		# noinspection PyUnboundLocalVariable
		i = starting_number + 10**m
		for _ in range(9):
			monkey_literals['humn'] = i
			if evaluate_job(monkey_jobs['root']):
				starting_number = i - 10**m  # subtract one of that magnitude for overshoot
				break
			i += 10**m
	return starting_number+1  # add 1 for the final overshoot subtraction


if __name__ == "__main__":
	print("part 1: ", int(evaluate_job(monkey_jobs['root'])))
	monkey_jobs['root'][1] = "="
	print("part 2: ", findSeed())
