"""Day 23 Advent_of_Code 2022"""
import os
from time import sleep
with open("input/day23.txt", 'r') as infile:
	elves = [[x, y] for y, row in enumerate(infile) for x, _ in enumerate(row.rstrip()) if _ == '#']
occ_space = {tuple(coord) for coord in elves}
moves = {
	'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0), 'NE': (1, -1), 'SE': (1, 1), 'SW': (-1, 1), 'NW': (-1, -1)
}
cardinals = [['NW', 'N', 'NE'], ['SE', 'S', 'SW'], ['SW', 'W', 'NW'], ['NE', 'E', 'SE']]
north = ['NW', 'N', 'NE']
south = ['SE', 'S', 'SW']
west = ['SW', 'W', 'NW']
east = ['NE', 'E', 'SE']
proposals = []
round_counts = []
movement_flag = True


def displayField():
	""" displays the field, of variable size in relation to elves

	:return: None
	"""
	count = 0
	min_x, max_x = min([each[0] for each in elves]), max([each[0] for each in elves])
	min_y, max_y = min([each[1] for each in elves]), max([each[1] for each in elves])
	d_field = [['#' if (x, y) in occ_space else '.' for x in range(min_x, max_x+1)] for y in range(min_y, max_y+1)]
	# os.system('cls')
	for each in d_field:
		tmp_string = "".join(each)
		count += tmp_string.count('.')
		# print(tmp_string)
	# sleep(.1)
	round_counts.append(count)
	return


def propose(elf):
	found = False
	# north check
	tmp_checks = [[sum(each) for each in zip(elf, moves[key])] for key in cardinals[0]]
	for coord in tmp_checks:
		if tuple(coord) in occ_space:
			found = True
			break
	else:
		proposal = tmp_checks[1]  # proposal move north # list
	# south check if for loop else's and found is True, proposal is south and we finish early
	# in the else clause if found is false, north keeps priority as we move on
	# if south check breaks we go on to west check
	tmp_checks = [[sum(each) for each in zip(elf, moves[key])] for key in cardinals[1]]
	for coord in tmp_checks:
		# if we found one here but found is still false, then north is the correct proposal and we can
		# end early
		if tuple(coord) in occ_space:
			if not found:
				# noinspection PyUnboundLocalVariable
				proposals.append(tuple(proposal))
				return
			else:  # found one north and south continue on to west
				break
	else:  # didn't find one south
		if found:  # didn't find one south but did find one north, propose south end early
			proposal = tmp_checks[1]  # proposal move south # list
			proposals.append(tuple(proposal))
			return
		else:  # didn't find one north or south, proposal is still north, move on to west
			pass
	# west checks
	tmp_checks = [[sum(each) for each in zip(elf, moves[key])] for key in cardinals[2]]
	for coord in tmp_checks:  # west checks
		if tuple(coord) in occ_space:  # found one west, but north south is True True, or False False
			if found:  # found in all three cardinals, move on to east
				break
			else:  # west is the first one we found, north is still correct proposal, end early
				# noinspection PyUnboundLocalVariable
				proposals.append(tuple(proposal))
				return
	else:  # didn't find one in west, if not found north is still best continue to east
		if found:  # found north and south not west
			proposal = tmp_checks[1]  # propose move west
			proposals.append(tuple(proposal))
			return
	# east check, at this  the only case is nothing is found in the previous three or everything found
	tmp_checks = [[sum(each) for each in zip(elf, moves[key])] for key in cardinals[3]]
	for coord in tmp_checks:
		if tuple(coord) in occ_space:  # found one here
			if found:  # found one in every direction cant move
				proposals.append(None)
			else:  # not found until east return north move
				# noinspection PyUnboundLocalVariable
				proposals.append(tuple(proposal))
			return
	else:  # if found propose east, if not didn't find any at all don't move
		if found:
			proposal = tmp_checks[1]
			proposals.append(tuple(proposal))
			return
		proposals.append(None)
		return


def movePrep():
	global occ_space
	global cardinals
	global movement_flag
	for elf in elves:
		propose(elf)
	cardinals.append(cardinals.pop(0))
	proposal_set = set()
	duplicates_set = set()
	for proposal in proposals:
		# if the proposal is in the proposal set it is a duplicate, and we will track duplicates and at teh end remove
		# the duplicates from the proposal set to cancel those moves
		# if its not in the proposal set we will add it to the proposal set
		if proposal in proposal_set:
			duplicates_set.add(proposal)  # add to duplicates set
		else:
			proposal_set.add(proposal)  # new proposal add to proposal set
	# remove duplicates set from proposal set to get all the valid moves to execute
	# put move logic
	correct_proposals = proposal_set - duplicates_set
	for index, elf in enumerate(elves):
		if proposals[index] in correct_proposals:
			elves[index] = list(proposals[index])  # overwrite elf position
	occ_space = {tuple(coord) for coord in elves}
	if len(correct_proposals) == 0:
		movement_flag = False
	proposals.clear()
	displayField()


def part2(rounds):
	displayField()
	while movement_flag:
		movePrep()
	print("part 1: ", round_counts[rounds])
	print("part 2: ", len(round_counts)-1)
	return


if __name__ == "__main__":
	part2(10)
