"""Day 03 Advent_of_Code 2023"""
with open("input/day03.txt", 'r') as infile:
	data = [line.rstrip() for line in infile]

move_dict = {'E': (0,1), 'SE': (1,1), 'S':(1,0), 'SW': (1,-1), 'W': (0,-1), 'NW': (-1,-1), 'N': (-1,0), 'NE': (-1,1)}

# def printMap():
# 	for each in data:
# 		print(each)


def product(values):
	"""Takes an iterable and creates a product of each element in the iterable

	:param values: List - (or other compatible iterable) to get the product of all elements
	:return: Int - Calculated product
	"""
	prod = 1
	for _ in values:
		prod *= _
	return prod


def sliceNumber(hits, part2=False):
	temp_dict = {}
	width = len(data[0])
	for coord in hits:
		point = coord[1]
		while point > -1 and data[coord[0]][point].isnumeric():
			point -= 1
		front = point+1
		point = coord[1]
		while point < width and data[coord[0]][point].isnumeric():
			point += 1
		end = point-1
		temp_dict.update({str([coord[0], front]): int(data[coord[0]][front:end+1])})
	if part2:
		if len(temp_dict) == 2:
			gear = product(temp_dict.values())
			temp_dict.clear()
			temp_dict.update({str(hits): gear})
		else:
			temp_dict.clear()
	return temp_dict


def trimCoords(candidate_coords):  # trims a list of 8 surrounding spaces to coordinates of numeric chars
	real_hits = []
	for coordinate in candidate_coords:
		try:
			if data[coordinate[0]][coordinate[1]].isnumeric():
				real_hits.append(coordinate)
		except IndexError:
			continue
	return real_hits


def detectNumbers(coord, part2=False):
	surround_coords = [[sum(pair) for pair in zip(coord, value)] for value in move_dict.values()]
	hits = trimCoords(surround_coords)  # get the actual number hits
	# next we need to process the numbers attached to our hits
	# return dictionary to update number_dict
	return sliceNumber(hits, part2)


def fun(part2=False):
	width = len(data[0])
	height = len(data)
	p = [-1, -1] # pointer
	# format key: (0,0) : int
	number_dict = {}
	# until end of our matrix
	while p != [height-1, width-1]:
		# for each row
		for h in range(height):
			p[0] += 1  # increment row
			p[1] = -1  # reset column for next pass
			# for each column in current row
			for w in range(width):
				p[1] += 1
				current_char = data[p[0]][p[1]]
				if not part2:
					# detector for special characters
					if (not current_char.isnumeric()) and current_char != '.':
						# call analyze number
						number_dict.update(detectNumbers(p))
				else:
					if current_char == '*':
						number_dict.update(detectNumbers(p, part2))
	return sum(number_dict.values())


if __name__ == "__main__":
	print("part 1: ", fun())
	print("part 2: ", fun(True))
