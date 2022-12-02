"""Day 07 Advent_of_Code 2015"""
with open("input/day07.txt", 'r') as infile:
	data = [tuple(line.rstrip().split(" -> ")) for line in infile]

# build register dictionary
registers = {instruction[-1]: None for instruction in data}
removal_set = set()  # set for instructions to be removed


def bit_cut(value, bits=16):
	""" takes an integer and cuts off the leading bits

	:param value: Int - any integer
	:param bits: Int - number of bits to return
	:return: Int - value cut down to bit limit
	"""
	return value & 2**bits-1


def evaluate_instruction(command):
	split_c = command[0].split(' ')
	if len(split_c) == 1:  # this is for the one outlier case where a register connects to another with no operation
		if registers[split_c[0]]:
			registers[command[1]] = registers[split_c[0]]
			removal_set.add(command)
		return
	match split_c[1]:
		case "AND":
			if split_c[0].isalpha():  # register1 AND register2 -> register3
				if registers[split_c[0]] is not None and registers[split_c[2]] is not None:
					registers[command[1]] = registers[split_c[0]] & registers[split_c[2]]
					removal_set.add(command)
			else:  # 1 and register
				if registers[split_c[2]] is not None:
					registers[command[1]] = int(split_c[0]) & registers[split_c[2]]
					removal_set.add(command)
		case "OR":  # register1 OR register2 -> register3
			if registers[split_c[0]] is not None and registers[split_c[2]] is not None:
				registers[command[1]] = registers[split_c[0]] | registers[split_c[2]]
				removal_set.add(command)
		case "LSHIFT":  # register1 LSHIFT value -> register2
			if registers[split_c[0]] is not None:
				registers[command[1]] = bit_cut(registers[split_c[0]] << int(split_c[2]))
				removal_set.add(command)
		case "RSHIFT":  # register RSHIFT value -> register2
			if registers[split_c[0]] is not None:
				registers[command[1]] = registers[split_c[0]] >> int(split_c[2])
				removal_set.add(command)
		case _:  # NOT register1 -> register2
			if registers[split_c[1]] is not None:
				registers[command[1]] = registers[split_c[1]] ^ 2**16-1
				removal_set.add(command)
	return


def part1(output_key):
	global data
	# get input registers filled and remove those instructions
	for instruction in data:
		if instruction[0].isnumeric():
			registers[instruction[-1]] = int(instruction[0])  # add input to labeled register
			removal_set.add(instruction)
	data = [each for each in data if each not in removal_set]  # rebuild instruction set
	while not registers[output_key]:  # until instructions are empty
		for instruction in data:
			evaluate_instruction(instruction)
		data = [each for each in data if each not in removal_set]  # rebuild after every full list pass
	return registers[output_key]


if __name__ == "__main__":
	print("part 1: ", part1('a'))
	# print("part 2: ")
