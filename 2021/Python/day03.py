"""Day 03 Advent_of_Code"""
with open("input/day03.txt", 'r') as infile:
    day03 = [line.rstrip() for line in infile]


def decode(bits):
    """Takes a long list of strings and decodes the binary by vertical columns, into a new
    single binary string based on the most common bit state of a vertical column in the data.

    :param bits: list - list of binary strings
    :return: 
    """
    gamma = []
    epsilon = []
    for digit in range(len(bits[0])):
        column = [bits[index][digit] for index in range(len(bits))]
        if column.count('1') > column.count('0'):
            gamma.append('1')
            epsilon.append('0')
            continue
        gamma.append('0')
        epsilon.append('1')
    gamma = "".join(gamma)
    epsilon = "".join(epsilon)
    return gamma, epsilon


def decode_oxy(bits):
    for digit in range(len(bits[0])):
        column = [bits[index][digit] for index in range(len(bits))]
        index = 0
        if column.count('1') >= column.count('0'):
            while index < len(bits):
                if bits[index][digit] == '0':
                    del bits[index]
                    index -= 1
                index += 1
            continue
        while index < len(bits):
            if bits[index][digit] == '1':
                del bits[index]
                index -= 1
            index += 1
    return bits[0]


def decode_c02(bits):
    for digit in range(len(bits[0])):
        column = [bits[index][digit] for index in range(len(bits))]
        index = 0
        if column.count('1') < column.count('0'):
            while index < len(bits) and len(bits) > 1:
                if bits[index][digit] == '0':
                    del bits[index]
                    index -= 1
                index += 1
            continue
        while index < len(bits) and len(bits) > 1:
            if bits[index][digit] == '1':
                del bits[index]
                index -= 1
            index += 1
    return bits[0]


def convert_calc(greeklist):
    gammastr = str(greeklist[0])
    epsilonstr = str(greeklist[1])
    return int(gammastr, 2) * int(epsilonstr, 2)


if __name__ == "__main__":
    print("part 1: ", convert_calc(decode(day03)))
    print("part 2: ", convert_calc((decode_oxy(day03.copy()), decode_c02(day03.copy()))))
