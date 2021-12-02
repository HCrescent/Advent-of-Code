"""Day 02 Advent_of_Code"""
with open("input/day02.txt", 'r') as infile:
    day02 = [line.strip().split() for line in infile]
    for element in day02:
        element[1] = int(element[1])


def sub_drive_part1(commands):
    depth = 0
    distance = 0
    for each in commands:
        if each[0] == "down":
            depth += each[1]
        elif each[0] == "up":
            depth -= each[1]
        elif each[0] == "forward":
            distance += each[1]
    return depth * distance


def sub_drive_part2(commands):
    depth = 0
    distance = 0
    aim = 0
    for each in commands:
        if each[0] == "down":
            aim += each[1]
        elif each[0] == "up":
            aim -= each[1]
        elif each[0] == "forward":
            if aim == 0:
                distance += each[1]
                continue
            distance += each[1]
            depth += aim * each[1]
    return depth * distance


if __name__ == "__main__":
    print(sub_drive_part1(day02))
    print(sub_drive_part2(day02))
