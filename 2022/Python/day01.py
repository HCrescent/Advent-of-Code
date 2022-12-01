"""Day 01 Advent_of_Code 2022"""
with open("input/day01.txt", 'r') as infile:
	data = [line.rstrip() for line in infile]


def fun(data):
	sums = []
	accumulator = 0
	for each in data:
		if each != '':
			accumulator += int(each)
		else:
			sums.append(accumulator)
			accumulator = 0
	return sums


if __name__ == "__main__":
	elf_list = fun(data)
	tmp = max(elf_list)
	print("part 1: ", tmp)
	elf_list.sort()
	print("part 2: ", sum(elf_list[-3:]))
