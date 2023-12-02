"""Day 02 Advent_of_Code 2023"""
with open("input/day02.txt", 'r') as infile:
	data = [line.rstrip() for line in infile]
data = [game[game.index(':')+2:] for game in data]


def compare_answer(red, green, blue):
	result = True
	answer_dict = {"red": 12, "green": 13, "blue": 14}
	if red > answer_dict["red"]:
		result = False
	if green > answer_dict["green"]:
		result = False
	if blue > answer_dict["blue"]:
		result = False
	return result


def part1(data_copy, part2=False):
	data_copy = [game.replace(', ', '; ').split("; ") for game in data_copy]
	data_copy = [[pair.split(' ') for pair in pull] for pull in data_copy]
	data_copy = [[[int(item) if item.isnumeric() else item for item in pair] for pair in game] for game in data_copy]
	for game in data_copy:
		game.sort()
	game_sum = 0
	red = 0
	blue = 0
	green = 0
	product_sum = 0
	for i, game in enumerate(data_copy):
		for pull in game[::-1]:
			if pull[1] == "red":
				red = pull[0]
				break
		for pull in game[::-1]:
			if pull[1] == "green":
				green = pull[0]
				break
		for pull in game[::-1]:
			if pull[1] == "blue":
				blue = pull[0]
				break
		if compare_answer(red, green, blue):
			game_sum += i+1
		if part2:
			product_sum += red * blue * green

	if part2:
		return product_sum
	return game_sum


if __name__ == "__main__":
	print("part 1: ", part1([_ for _ in data]))
	print("part 2: ", part1([_ for _ in data], True))
