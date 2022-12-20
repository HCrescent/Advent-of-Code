"""Day 20 Advent_of_Code 2022"""
with open("input/day20.txt", 'r') as infile:
	data = [int(line.rstrip()) for line in infile]
enumeration = [i for i in range(len(data))]
print(data)
print(enumeration)


def fun():
	msg_len = len(enumeration)
	for procession in range(msg_len):
		target_adr = enumeration.index(procession)
		tmp_dat = data.pop(target_adr)
		tmp_enum = enumeration.pop(target_adr)
		if tmp_dat < 0:
			new_adr = ((target_adr + tmp_dat) % msg_len) - 1
		else:
			new_adr = (target_adr + tmp_dat) % msg_len
			if tmp_dat + target_adr > msg_len:
				new_adr += 1 * ((target_adr + tmp_dat)//msg_len)  # plus one for each wrap around
		if new_adr == -1:  # insert -1 doesnt work the same as slicing
			data.append(tmp_dat)
			enumeration.append(tmp_enum)
			print(procession)
			print(data)
			print(enumeration)
			print()
			continue
		if new_adr < 0:
			new_adr += 1
		data.insert(new_adr, tmp_dat)
		enumeration.insert(new_adr, tmp_enum)
		print(procession)
		print(data)
		print(enumeration)
		print()
	pass


if __name__ == "__main__":
	test = [1, 2, 3]
	test.insert(-2, 4)
	print(test)
	fun()
	# print("part 1: ")
	# print("part 2: ")
