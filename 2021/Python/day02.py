"""Day 02 Advent_of_Code"""
with open("input/day02.txt", 'r') as infile:
    # strip and split each line in order to day02 to become a list of lists
    day02 = [line.strip().split() for line in infile]
    # turn number strings into integers
    for element in day02:
        element[1] = int(element[1])


def sub_drive_part1(commands):
    """Takes a list of movement instructions and calculates submarine position.

    :param commands: list - list of lists containing sub movement commands and associated value
    :return: int - depth multiplied by distance as requested for the solution input
    """

    depth = 0
    distance = 0
    # for each sub-list in our list of lists commands
    for each in commands:
        # rudimentary switch case
        # if 'down' add value to our depth
        if each[0] == "down":
            depth += each[1]
        # if 'up' sub value from our depth
        elif each[0] == "up":
            depth -= each[1]
        # if 'forward' add value to our horizontal distance
        elif each[0] == "forward":
            distance += each[1]
    return depth * distance


def sub_drive_part2(commands):
    """Takes a list of movement instructions and calculates submarine position more accurately.

    :param commands: list - list of lists containing sub movement commands and associated value
    :return: int - depth multiplied by distance as requested for the solution input
    """

    depth = 0
    distance = 0
    # in order to more accurately simulate our path we will use aim when moving forward to see if we are
    aim = 0
    # for each sub-list in our list of lists commands
    for each in commands:
        # rudimentary switch case
        # if 'down', adjust aim in the positive direction
        if each[0] == "down":
            aim += each[1]
        # if 'up', adjust aim in the negative direction
        elif each[0] == "up":
            aim -= each[1]
        # if 'forward' we propel the sub in the direction of our aim
        elif each[0] == "forward":
            # extra clause to avoid losing our value when multiplying by 0
            if aim == 0:
                # add value to horizontal distance, end loop early
                distance += each[1]
                continue
            distance += each[1]
            # add provided formula for depth change, aim * value
            depth += aim * each[1]
    return depth * distance


if __name__ == "__main__":
    print("part 1: ", sub_drive_part1(day02))
    print("part 2: ", sub_drive_part2(day02))
