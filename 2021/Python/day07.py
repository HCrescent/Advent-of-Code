"""Day 07 Advent_of_Code"""
with open("input/day07.txt", 'r') as infile:
    data = list(infile)
crabs = data[0].strip().split(',')
crabs = [int(each) for each in crabs]
TESTCASE_RANGE = max(crabs) - min(crabs)


def fuel_cost(position, part2):
    if part2:
        sigma_cost = [(abs(position-each)*(abs(position-each)+1))//2 for each in crabs]
        return sum(sigma_cost)
    cost = [abs(position - each) for each in crabs]
    return sum(cost)


def run_gauntlet(part2, test_range=TESTCASE_RANGE):
    all_results = [fuel_cost(horizontal_position, part2) for horizontal_position in range(test_range)]
    return min(all_results)


if __name__ == "__main__":
    print("part 1: ", run_gauntlet(False))
    print("part 2: ", run_gauntlet(True))
