"""Day 20 Advent_of_Code 2022"""
with open("input/day20.txt", 'r') as infile:
	data = [int(line.rstrip()) for line in infile]
enumeration = [i for i in range(len(data))]
data_p2 = [_ for _ in data]  # copy of data for part 2


def mix():
	""" mixes the data by shifting data based on its value

	:return: None
	"""
	msg_len = len(enumeration)
	for procession in range(msg_len):  # for every number in data
		target_adr = enumeration.index(procession)  # get the address of the target
		# pop the data and its tracking number
		tmp_dat = data.pop(target_adr)
		tmp_enum = enumeration.pop(target_adr)
		if tmp_dat != 0:
			new_adr = (target_adr + tmp_dat) % (msg_len-1)
		else:  # edge case for zero
			new_adr = target_adr
		# insert data and tracking number
		data.insert(new_adr, tmp_dat)
		enumeration.insert(new_adr, tmp_enum)
	return


def part1():
	# mix once and get sum of specified indexes
	mix()
	start_point = data.index(0)
	msg = len(data)
	a = data[(start_point + 1000) % msg]
	b = data[(start_point + 2000) % msg]
	c = data[(start_point + 3000) % msg]
	return a+b+c


def part2():
	# mix ten times and get sum of specified indexes
	for _ in range(10):
		mix()
	start_point = data.index(0)
	msg = len(data)
	a = data[(start_point + 1000) % msg]
	b = data[(start_point + 2000) % msg]
	c = data[(start_point + 3000) % msg]
	return a+b+c


if __name__ == "__main__":
	print("part 1: ", part1())
	key = 811589153
	data = [each * key for each in data_p2]  # reinitialize starting data
	enumeration = [i for i in range(len(data))]  # reinitialize starting enumeration
	print("part 2: ", part2())
