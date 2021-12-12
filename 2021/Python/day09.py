"""Day 09 Advent_of_Code 2021"""
with open("input/day09.txt", 'r') as infile:
    matrix_map = [list(line.rstrip()) for line in infile]
for i, each in enumerate(matrix_map):
    matrix_map[i] = list(map(int, each))


def iterate_matrix(matrix):
    risk_sums = 0
    areas = []
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            risk, area = add_neighbors(matrix, x, y)
            risk_sums += risk
            areas.append(area)
    areas.sort()
    return risk_sums, areas


def add_neighbors(matrix, x, y):
    risk_level = 0
    area = 0
    num = matrix[x][y]
    # core case with largest amount of executions, always has 4 neighbors
    if 0 < x < len(matrix)-1 and 0 < y < len(matrix[x])-1:  # case for matrix[x][y] has 4 neighbors.
        #          west                         east                    south                   north
        if num < matrix[x][y-1] and num < matrix[x][y+1] and num < matrix[x+1][y] and num < matrix[x-1][y]:
            risk_level = 1 + num
    # top edge case, always 3 neighbors: west east south
    elif x == 0 and 0 < y < len(matrix[x])-1:
        if num < matrix[x][y-1] and num < matrix[x][y+1] and num < matrix[x+1][y]:
            risk_level = 1 + num
    # right edge case, always 3 neighbors: west south north
    elif 0 < x < len(matrix)-1 and y == len(matrix[x])-1:
        if num < matrix[x][y-1] and num < matrix[x+1][y] and num < matrix[x-1][y]:
            risk_level = 1 + num
    # bottom edge case, always 3 neighbors: west east north
    elif x == len(matrix)-1 and 0 < y < len(matrix[x])-1:
        if num < matrix[x][y-1] and num < matrix[x][y+1] and num < matrix[x-1][y]:
            risk_level = 1 + num
    # left edge case, always 3 neighbors: east south north
    elif 0 < x < len(matrix)-1 and y == 0:
        if num < matrix[x][y+1] and num < matrix[x+1][y] and num < matrix[x-1][y]:
            risk_level = 1 + num
    # top left corner case, always 2 neighbors: east south
    elif x == 0 and y == 0:
        if num < matrix[x][y+1] and num < matrix[x+1][y]:
            risk_level = 1 + num
    # top right corner case, always 2 neighbors: west south
    elif x == 0 and y == len(matrix[x])-1:
        if num < matrix[x][y-1] and num < matrix[x+1][y]:
            risk_level = 1 + num
    # bottom left corner case, always 2 neighbors: east north
    elif x == len(matrix)-1 and y == 0:
        if num < matrix[x][y+1] and num < matrix[x-1][y]:
            risk_level = 1 + num
    # bottom right corner case, always 2 neighbors: west north
    elif x == len(matrix)-1 and y == len(matrix[x])-1:
        if num < matrix[x][y-1] and num < matrix[x-1][y]:
            risk_level = 1 + num
    if risk_level > 0:
        # MAP THAT BASIN
        record = {}
        record = basin_mapper(matrix, x, y, record)
        area = len(record)
    return risk_level, area


def north(matrix, x, y, record):
    # north is < 9 and not a node
    return matrix[x-1][y] < 9 and record.get(f"m:{x-1},{y}", 1)


def east(matrix, x, y, record):
    # east is < 9 and not a node
    return matrix[x][y+1] < 9 and record.get(f"m:{x},{y+1}", 1)


def south(matrix, x, y, record):
    # south is < 9 and not a node
    return matrix[x+1][y] < 9 and record.get(f"m:{x+1},{y}", 1)


def west(matrix, x, y, record):
    # west is below 9 and not a node
    return matrix[x][y-1] < 9 and record.get(f"m:{x},{y-1}", 1)


def basin_mapper(matrix, x, y, record):
    """RECURSION BABY, We start at our basin origin, record a key-string for our legal node and then step in to the
    next movement.

    :param matrix: list - list of lists matrix
    :param x: int - x coordinate in our matrix
    :param y: int - y coordinate in our matrix
    :param record: dict - dictionary of nodes : False for bool key checks while pathing
    :return: dict - the most up to date record of nodes
    """
    if 0 < x < len(matrix)-1 and 0 < y < len(matrix[x])-1:  # case for matrix[x][y] has 4 neighbors.
        record[f"m:{x},{y}"] = False
        if west(matrix, x, y, record):
            record = basin_mapper(matrix, x, y-1, record)
        if east(matrix, x, y, record):
            record = basin_mapper(matrix, x, y+1, record)
        if south(matrix, x, y, record):
            record = basin_mapper(matrix, x+1, y, record)
        if north(matrix, x, y, record):
            record = basin_mapper(matrix, x-1, y, record)
    # top edge case, always 3 neighbors: west east south
    elif x == 0 and 0 < y < len(matrix[x])-1:
        record[f"m:{x},{y}"] = False
        if west(matrix, x, y, record):
            record = basin_mapper(matrix, x, y-1, record)
        if east(matrix, x, y, record):
            record = basin_mapper(matrix, x, y+1, record)
        if south(matrix, x, y, record):
            record = basin_mapper(matrix, x+1, y, record)
    # right edge case, always 3 neighbors: west south north
    elif 0 < x < len(matrix)-1 and y == len(matrix[x])-1:
        record[f"m:{x},{y}"] = False
        if west(matrix, x, y, record):
            record = basin_mapper(matrix, x, y-1, record)
        if south(matrix, x, y, record):
            record = basin_mapper(matrix, x+1, y, record)
        if north(matrix, x, y, record):
            record = basin_mapper(matrix, x-1, y, record)
    # bottom edge case, always 3 neighbors: west east north
    elif x == len(matrix)-1 and 0 < y < len(matrix[x])-1:
        record[f"m:{x},{y}"] = False
        if west(matrix, x, y, record):
            record = basin_mapper(matrix, x, y-1, record)
        if east(matrix, x, y, record):
            record = basin_mapper(matrix, x, y+1, record)
        if north(matrix, x, y, record):
            record = basin_mapper(matrix, x-1, y, record)
    # left edge case, always 3 neighbors: east south north
    elif 0 < x < len(matrix)-1 and y == 0:
        record[f"m:{x},{y}"] = False
        if east(matrix, x, y, record):
            record = basin_mapper(matrix, x, y+1, record)
        if south(matrix, x, y, record):
            record = basin_mapper(matrix, x+1, y, record)
        if north(matrix, x, y, record):
            record = basin_mapper(matrix, x-1, y, record)
    # top left corner case, always 2 neighbors: east south
    elif x == 0 and y == 0:
        record[f"m:{x},{y}"] = False
        if east(matrix, x, y, record):
            record = basin_mapper(matrix, x, y+1, record)
        if south(matrix, x, y, record):
            record = basin_mapper(matrix, x+1, y, record)
    # top right corner case, always 2 neighbors: west south
    elif x == 0 and y == len(matrix[x])-1:
        record[f"m:{x},{y}"] = False
        if west(matrix, x, y, record):
            record = basin_mapper(matrix, x, y-1, record)
        if south(matrix, x, y, record):
            record = basin_mapper(matrix, x+1, y, record)
    # bottom left corner case, always 2 neighbors: east north
    elif x == len(matrix)-1 and y == 0:
        record[f"m:{x},{y}"] = False
        if east(matrix, x, y, record):
            record = basin_mapper(matrix, x, y+1, record)
        if north(matrix, x, y, record):
            record = basin_mapper(matrix, x-1, y, record)
    # bottom right corner case, always 2 neighbors: west north
    elif x == len(matrix)-1 and y == len(matrix[x])-1:
        record[f"m:{x},{y}"] = False
        if west(matrix, x, y, record):
            record = basin_mapper(matrix, x, y-1, record)
        if north(matrix, x, y, record):
            record = basin_mapper(matrix, x-1, y, record)
    return record


if __name__ == "__main__":
    risk_sum, basin_areas = iterate_matrix(matrix_map)
    print("part 1: ", risk_sum)
    print("part 2: ", basin_areas[-1] * basin_areas[-2] * basin_areas[-3])
