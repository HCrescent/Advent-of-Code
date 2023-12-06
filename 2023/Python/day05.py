"""Day 05 Advent_of_Code 2023"""
with open("input/day05.txt", 'r') as infile:
	data = [line.rstrip().split('\n') for line in infile]
data = [row.split() for each in data for row in each]
seed_dict = {'seeds': list(map(int, data[0][1:]))}
key_dict = {}
conversion_dict = {}
data.pop(0)
data.append([])
key_count = 0
for i, row in enumerate(data):
	if not row:
		try:
			key = data[i+1][0]
		except IndexError:
			break
		key_dict.update({key_count: key})
		key_count += 1
		end = data[i+1:].index([]) + i
		numbers = [list(map(int, each)) for each in data[i+2:end+1]]
		conversion_dict.update({key:numbers})


def fun(part2=False):
	if part2:
		new_seeds = []
		for index in range(len(seed_dict['seeds']))[::2]:
			start = seed_dict['seeds'][index]
			ending = seed_dict['seeds'][index+1]
			for number in range(start, start+ending):
				new_seeds.append(number)
		seed_dict.update({'seeds': new_seeds})

	final_value = 1000000000000000000000
	for seed in seed_dict['seeds']:
		for king_index in range(len(key_dict)):
			for conversion_map in conversion_dict[key_dict[king_index]]:
				# if the seed number is convertible
				if conversion_map[1] <= seed <= conversion_map[1] + conversion_map[2]:
					conversion = seed + (conversion_map[0] - conversion_map[1])
					seed = conversion
					break
		if seed < final_value:
			final_value = seed
	return final_value


if __name__ == "__main__":
	print("part 1: ", fun())
	print("part 2: ", fun(True)-1)
