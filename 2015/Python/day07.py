"""Day 07 Advent_of_Code 2015"""
with open("input/day07.txt", 'r') as infile:
	data = [tuple(line.rstrip().split(" -> ")) for line in infile]
data_copy = [each for each in data]  # copy of data for part 2
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


def evaluate_instruction(command, reg_dict):
	split_c = command[0].split(' ')
	if len(split_c) == 1:  # this is for the one outlier case where a register connects to another with no operation
		if reg_dict[split_c[0]]:
			reg_dict[command[1]] = reg_dict[split_c[0]]
			removal_set.add(command)
		return
	match split_c[1]:
		case "AND":
			if split_c[0].isalpha():  # register1 AND register2 -> register3
				if reg_dict[split_c[0]] is not None and reg_dict[split_c[2]] is not None:
					reg_dict[command[1]] = reg_dict[split_c[0]] & reg_dict[split_c[2]]
					removal_set.add(command)
			else:  # 1 and register
				if reg_dict[split_c[2]] is not None:
					reg_dict[command[1]] = int(split_c[0]) & reg_dict[split_c[2]]
					removal_set.add(command)
		case "OR":  # register1 OR register2 -> register3
			if reg_dict[split_c[0]] is not None and reg_dict[split_c[2]] is not None:
				reg_dict[command[1]] = reg_dict[split_c[0]] | reg_dict[split_c[2]]
				removal_set.add(command)
		case "LSHIFT":  # register1 LSHIFT value -> register2
			if reg_dict[split_c[0]] is not None:
				reg_dict[command[1]] = bit_cut(reg_dict[split_c[0]] << int(split_c[2]))
				removal_set.add(command)
		case "RSHIFT":  # register RSHIFT value -> register2
			if reg_dict[split_c[0]] is not None:
				reg_dict[command[1]] = reg_dict[split_c[0]] >> int(split_c[2])
				removal_set.add(command)
		case _:  # NOT register1 -> register2
			if reg_dict[split_c[1]] is not None:
				reg_dict[command[1]] = reg_dict[split_c[1]] ^ 2**16-1
				removal_set.add(command)
	return


def part1(output_key, reg_dict):
	global data
	# get input reg_dict filled and remove those instructions
	for instruction in data:
		if instruction[0].isnumeric():
			reg_dict[instruction[-1]] = int(instruction[0])  # add input to labeled register
			removal_set.add(instruction)
	data = [each for each in data if each not in removal_set]  # rebuild instruction set
	while not reg_dict[output_key]:  # until instructions are empty
		for instruction in data:
			evaluate_instruction(instruction, reg_dict)
		data = [each for each in data if each not in removal_set]  # rebuild after every full list pass
	return reg_dict[output_key]


def part2(output_key, reg_dict):
	global data_copy
	# get input reg_dict filled and remove those instructions
	for instruction in data_copy:
		if instruction[0].isnumeric():
			reg_dict[instruction[-1]] = int(instruction[0])  # add input to labeled register
			removal_set.add(instruction)
	data_copy = [each for each in data_copy if each not in removal_set]  # rebuild instruction set
	registers['b'] = new_b
	while not reg_dict[output_key]:  # until instructions are empty
		for instruction in data_copy:
			evaluate_instruction(instruction, reg_dict)
		data_copy = [each for each in data_copy if each not in removal_set]  # rebuild after every full list pass
	return reg_dict[output_key]


if __name__ == "__main__":
	print("part 1: ", part1('a', registers))
	new_b = registers['a']
	registers = {key: None for key, value in registers.items()}
	removal_set.clear()
	print("part 2: ", part2('a', registers))
