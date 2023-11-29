"""Day 02 Advent_of_Code 2019"""
with open("input/day02.txt", 'r') as infile:
	data = [int(each) for each in infile.read().strip().rsplit(',')]

def ALU(program, initial_parameters):
	program[1], program[2] = initial_parameters
	pointer = 0
	while program[pointer] != 99:
		input1 = program[pointer+1]
		input2 = program[pointer+2]
		output = program[pointer+3]
		match program[pointer]:
			case 1:  # add
				program[output] = program[input1] + program[input2]
			case 2:  # multiply
				program[output] = program[input1] * program[input2]
			case _:  # nothing
				pass
		pointer += 4
	return program[0]

def part2(target):
	for noun in range(0, 100):
		for verb in range(0, 100):
			if ALU([_ for _ in data], [noun, verb]) == target:
				return 100 * noun + verb
	pass



if __name__ == "__main__":
	datacopy = [_ for _ in data]
	print("part 1: ", ALU(datacopy, [12, 2]))
	print("part 2: ", part2(19690720))
