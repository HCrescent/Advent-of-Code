"""Day 04 Advent_of_Code 2025"""
with open("input/day04.txt", 'r') as infile:
	data = [list(line.rstrip()) for line in infile]
mutations = [[1,1], [1,0], [1,-1], [0,1], [0,-1], [-1,1], [-1,0], [-1,-1]]

# def part1():
# 	total = 0
# 	for x in range(len(data)):
# 		for y in range(len(data[x])):
# 			if data[x][y] == '@':
# 				humans = 0
# 				surrounding = [[pair[0]+x, pair[1]+y] for pair in mutations]
# 				for coordinate in surrounding:
# 					if min(coordinate) >= 0:
# 						try:
# 							if data[coordinate[0]][coordinate[1]] == '@':
# 								humans += 1
# 						except IndexError:
# 							continue
# 				if humans < 4:
# 					total += 1
# 	return total


def part2():
	total = 0
	pass_targets = []
	for x in range(len(data)):
		for y in range(len(data[x])):
			if data[x][y] == '@':
				humans = 0
				surrounding = [[pair[0]+x, pair[1]+y] for pair in mutations]
				for coordinate in surrounding:
					if min(coordinate) >= 0: #stop allowing negative indexing for wrap around false positives
						try:
							if data[coordinate[0]][coordinate[1]] == '@':
								humans += 1
						# ignore out of bounds checks
						except IndexError:
							continue
				if humans < 4:
					total += 1
					pass_targets.append([x,y])
	return total, pass_targets


if __name__ == "__main__":
	print("part 1: ", part2()[0])

	removal_total = 0
	not_empty = [0]
	while not_empty:
		removed, targets = part2()
		removal_total += removed
		not_empty = targets
		for each in targets:
			data[each[0]][each[1]] = '.'

	print("part 2: ", removal_total)
