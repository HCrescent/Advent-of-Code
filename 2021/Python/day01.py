"""Day 01 Advent_of_Code"""
with open("input/day01.txt", 'r') as infile:
    # int() the string returned by rstrip() for each line
    day01 = [int(line.rstrip()) for line in infile]


def depth_increase_counter(depth_readings):
    """Takes a list of integers and counts the increases from list[n]->list[n+1].

    :param depth_readings: list of integers representing depth measurements
    :return: int - number of times the depth increases from previous depth
    """

    counter = 0
    # stop at length -1 so we can start at 0 and not exceed list index on final check
    for index in range(len(depth_readings)-1):
        if depth_readings[index] < depth_readings[index+1]:
            counter += 1
    return counter


def measurement_window(depth_readings):
    """Reads list with three-measurement sliding window and returning new list of sums.

    :param depth_readings: list of integers representing depth measurements
    :return: list - new list of sums of the sliding measurement window
    """

    new_list = []
    # stop at length -2 so we can start at 0 and not exceed list index on final check
    for index in range(len(depth_readings)-2):
        # append the window sum
        new_list.append(depth_readings[index] + depth_readings[index+1] + depth_readings[index+2])
    return new_list


if __name__ == "__main__":
    print("part 1: ", depth_increase_counter(day01))
    print("part 2: ", depth_increase_counter(measurement_window(day01)))
