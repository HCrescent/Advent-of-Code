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
	"=": lambda a, b: a == b
}


def evaluate_job(instruction):
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
	return operator_lambdas[instruction[1]](literal_1, literal_2)


def reverse():
	value = evaluate_job(monkey_jobs[monkey_jobs['root'][2]])
	i = 3342154812500
	while True:
		monkey_literals['humn'] = i
		if evaluate_job(monkey_jobs['root']):
			break
		i += 1
	print(i)


if __name__ == "__main__":
	print("part 1: ", evaluate_job(monkey_jobs['root']))
	monkey_jobs['root'][1] = "="
	# print("part 2: ")
	reverse()
