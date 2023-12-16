"""Day 04 Advent_of_Code 2023"""
# I intended to fix this code, but then college finals interrupted my participation in AoC, this code works, but
# what I recall is that due to confusion there was extraneous processing done, I no longer remember the problem or
# logic path used to solve it so because this is just personal exercise I will leave it as is, I don't do extensive
# commenting for AoC due to the racing nature of the competition for better code practices check my project euler repo
with open("input/day04.txt", 'r') as infile:
	data = [line.rstrip()[8:].split(' | ') for line in infile]
data  = [[card[0].split(' '), card[1].split(' ')] for card in data]
for card in data:
	for section in card:
		for i in range(len(section))[::-1]:
			if section[i] == '' or section[i] == ':':
				section.pop(i)

for card in data:
	for section in card:
		for i in range(len(section)):
			if section[i].isnumeric():
				section[i] = int(section[i])


def point_value(setting):
	match len(setting):
		case 0:
			point = 0
		case 1:
			point = 1
		case 2:
			point = 2
		case _:
			point = (2**(len(setting)-1))
	return point


def fun(part2=False):
	point_sum = 0
	matches_record = []
	for card in data:
		set1 = set(card[0])
		set2 = set(card[1])
		set_result = set1 & set2
		card_point = point_value(set_result)
		matches_record.append(len(set_result))
		point_sum += card_point
	card_total_dict = {str(_): 0 for _ in range(len(data))}
	if part2:
		for n, card in enumerate(data):
			for total in range(card_total_dict[str(n)]+1):
				for number in range(matches_record[n]):
					card_total_dict[str(n+number+1)] += 1
		return sum(card_total_dict.values()) + len(card_total_dict)


	return point_sum


if __name__ == "__main__":
	print("part 1: ", fun())
	print("part 2: ", fun(True))
