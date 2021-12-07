"""Day 06 Advent_of_Code"""
REPRODUCTIVE_CYCLE = 7
MATURATION_TIME = 2

with open("input/day06.txt", 'r') as infile:
    data = list(infile)
starting_population = data[0].strip().split(',')
starting_population = [int(each) for each in starting_population]


def initialize_census():
    # initialize census array for any constant cycle and mature time
    fish_census = []
    for _ in range(MATURATION_TIME + REPRODUCTIVE_CYCLE):
        fish_census.append(0)
    # initialize starting population based on data
    for state in starting_population:
        fish_census[state] += 1
    return fish_census


def age(days):
    for _ in range(days):
        zero_population = census.pop(0)
        census.append(zero_population)
        census[REPRODUCTIVE_CYCLE - 1] += zero_population
        print(census)
    pass


if __name__ == "__main__":
    census = initialize_census()
    age(80)
    print("part 1: ", sum(census))
    census = initialize_census()
    age(256)
    print("part 2: ", sum(census))
