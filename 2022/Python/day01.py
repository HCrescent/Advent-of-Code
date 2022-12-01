"""Day 01 Advent_of_Code 2022"""
with open("input/day01.txt", 'r') as infile:
	data = [int(line.rstrip()) if line != '\n' else 0 for line in infile]

if __name__ == "__main__":
	elf_list = []
	accumulator = 0
	for each in data:
		if each:
			accumulator += each
		else:
			elf_list.append(accumulator)
			accumulator = 0
	print("part 1: ", max(elf_list))
	elf_list.sort()
	print("part 2: ", sum(elf_list[-3:]))
