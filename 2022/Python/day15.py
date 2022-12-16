"""Day 15 Advent_of_Code 2022"""
with open("input/day15.txt", 'r') as infile:
	data = [line.rstrip().split(": closest ") for line in infile]
sensors = [tuple(int(num) for num in each[0].replace("x=", "")[10:].replace("y=", "").split(', ')) for each in data]
beacons = [tuple(int(num) for num in each[1].replace("x=", "")[13:].replace("y=", "").split(', ')) for each in data]


def getDistance(sensor, beacon):
	return abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])

# scope notes and ideas
# what is the leftmost bound? first thought is leftmost beacon, but example shows that two sensors that would extend
# well past that, so next thought is adding some sort of Manhattan distance to the the leftmost bound? unsure if will
# work, run into a thought problem, what if a sensor with a large Manhattan is far to the left of a leftmost beacon,
# therefore, we must find the leftmost object, whether beacon or sensor, PLUS that Manhattan distance? which Manhattan
# distance? but wait if the beacon is left most object, known spaces to the left will still be from a leftmost sensor
# therefore i think we can go with leftmost sensor plus Manhattan distance as the overall left bound and mirrored for
# right bound, hopefully that doesnt overload


def leftmostRightmost():
	""" returns the best choice indexes for min and max sensors for bound calculation

	:return: List - min and max indexes in global data set for sensors
	"""
	SB_pairs = list(zip(sensors, beacons))
	x_list = [each[0] for each in sensors]
	tmp_min, tmp_max = min(x_list), max(x_list)
	if x_list.count(tmp_min) == 1:
		min_i = x_list.index(tmp_min)
	else:  # figure out which has the larger Manhattan distance
		ties_indexes = [i for i, x in enumerate(x_list) if x == tmp_min]  # get all tied leftmost sensors indexes
		manhattans = [getDistance(*SB_pairs[index]) for index in ties_indexes]  # get all manhattans to their beacon
		min_i = ties_indexes[manhattans.index(max(manhattans))]  # ties don't matter here for max, gets final index
	if x_list.count(tmp_max) == 1:
		max_i = x_list.index(tmp_max)
	else:  # figure out which has the larger Manhattan distance
		ties_indexes = [i for i, x in enumerate(x_list) if x == tmp_max]  # get all tied rightmost sensors indexes
		manhattans = [getDistance(*SB_pairs[index]) for index in ties_indexes]  # get all manhattans to their beacon
		max_i = ties_indexes[manhattans.index(max(manhattans))]  # ties don't matter here for max, gets final index
	return min_i, max_i


def knownSpaces(y_row):
	manhattans = []
	return


if __name__ == "__main__":
	print("part 1: ", leftmostRightmost())
	# print("part 2: ")
