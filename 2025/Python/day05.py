"""Day 05 Advent_of_Code 2025"""
with open("input/day05.txt", 'r') as infile:
	data, tests = infile.read().split('\n\n')
	data = data.split('\n')
	data = [list(map(int, each)) for each in [line.split('-') for line in data]]
	tests = [int(each) for each in tests.split('\n')[:-1]]


def part1():
	total_fresh = 0
	for target in tests:
		for id_left, id_right in data:
			if target >= id_left:
				if target <= id_right:
					total_fresh += 1
					break
	return total_fresh


def part2():
	total_fresh = 0
	data.sort()
	new_inventory = [data.pop(0)]
	while len(data):
		for id_left, id_right in data:
			# combine
			if id_left <= new_inventory[-1][1] <= id_right:
				new_inventory[-1][1] = id_right
				data.remove([id_left, id_right])
				break
			# swallow
			if id_left >= new_inventory[-1][0] and id_right <= new_inventory[-1][1]:
				data.remove([id_left, id_right])
				break
		else:
			new_inventory.append(data.pop(0))

	for each in new_inventory:
		total_fresh += (each[1] - each[0])+1
	return total_fresh


if __name__ == "__main__":
	print("part 1: ", part1())
	print("part 2: ", part2())
