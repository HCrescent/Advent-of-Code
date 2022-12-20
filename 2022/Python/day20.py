"""Day 20 Advent_of_Code 2022"""
with open("input/day20.txt", 'r') as infile:
	data = [int(line.rstrip()) for line in infile]


def mix():
	enumeration = [i for i in range(len(data))]
	msg_len = len(enumeration)
	for procession in range(msg_len):
		target_adr = enumeration.index(procession)
		tmp_dat = data.pop(target_adr)
		tmp_enum = enumeration.pop(target_adr)
		if tmp_dat != 0:
			new_adr = (target_adr + tmp_dat) % (msg_len-1)
		else:
			new_adr = target_adr
		data.insert(new_adr, tmp_dat)
		enumeration.insert(new_adr, tmp_enum)
	pass


if __name__ == "__main__":
	mix()
	start_point = data.index(0)
	msg = len(data)
	a = data[(start_point + 1000) % msg]
	b = data[(start_point + 2000) % msg]
	c = data[(start_point + 3000) % msg]
	print("part 1: ", a+b+c)
	# print("part 2: ")
