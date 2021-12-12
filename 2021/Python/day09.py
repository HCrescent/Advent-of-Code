"""Day 09 Advent_of_Code 2021"""
import copy

with open("input/day09.txt", 'r') as infile:
    matrix_map = [list(line.rstrip()) for line in infile]
for i, each in enumerate(matrix_map):
    matrix_map[i] = list(map(int, each))


def display_matrix(matrix):
    for _ in range(len(matrix)):
        print(matrix[_])


def iterate_matrix(matrix, part2=False):
    risk_sums = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            risk_sums += add_neighbors(matrix, x, y, part2)
    return risk_sums


def add_neighbors(matrix, x, y, part2=False):
    risk_level = 0
    num = matrix[x][y]
    # non edge cases, core case with largest amount of executions, always has 4 neighbors
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
    if risk_level > 0 and part2:
        record = {}
        basin_mapper(matrix, x, y, record)
    return risk_level


def basin_mapper(matrix, x, y, record, old_x=None, old_y=None):
    old_node = [old_x, old_y]
    # our old x and old y here are to prevent accidental backtracking in our recursion
    # non edge cases, core case with largest amount of executions, always has 4 neighbors
    if 0 < x < len(matrix) - 1 and 0 < y < len(matrix[x]) - 1:  # case for matrix[x][y] has 4 neighbors.
        if matrix[x][y-1] < 9 and [x, y-1] != old_node and f"m:{x},{y}" not in record.keys():  # west is below 9 and not our previous node
            basin_mapper(matrix, x, y-1, x, y)
        if matrix[x][y+1] < 9 and [x, y+1] != old_node:  # east is < 9 and not previous node
            basin_mapper(matrix, x, y+1, x, y)
        if matrix[x+1][y] < 9 and [x+1, y] != old_node:  # south is < 9 and not previous node
            basin_mapper(matrix, x+1, y, x, y)
        if matrix[x-1][y] < 9 and [x-1, y] != old_node:  # north is < 9 and not previous node
            basin_mapper(matrix, x-1, y, x, y)
    # top edge case, always 3 neighbors: west east south
    elif x == 0 and 0 < y < len(matrix[x]) - 1:
        if matrix[x][y - 1] < 9 and [x, y-1] != old_node:  # west is below 9 and not our previous node
            basin_mapper(matrix, x, y-1, x, y)
        if matrix[x][y+1] < 9 and [x, y+1] != old_node:  # east is < 9 and not previous node
            basin_mapper(matrix, x, y+1, x, y)
        if matrix[x+1][y] < 9 and [x+1, y] != old_node:  # south is < 9 and not previous node
            basin_mapper(matrix, x+1, y, x, y)
    # right edge case, always 3 neighbors: west south north
    elif 0 < x < len(matrix) - 1 and y == len(matrix[x]) - 1:
        if matrix[x][y-1] < 9 and [x, y-1] != old_node:  # west is below 9 and not our previous node
            basin_mapper(matrix, x, y-1, x, y)
        if matrix[x+1][y] < 9 and [x+1, y] != old_node:  # south is < 9 and not previous node
            basin_mapper(matrix, x+1, y, x, y)
        if matrix[x-1][y] < 9 and [x-1, y] != old_node:  # north is < 9 and not previous node
            basin_mapper(matrix, x-1, y, x, y)
    # bottom edge case, always 3 neighbors: west east north
    elif x == len(matrix) - 1 and 0 < y < len(matrix[x]) - 1:
        if matrix[x][y-1] < 9 and [x, y-1] != old_node:  # west is below 9 and not our previous node
            basin_mapper(matrix, x, y-1, x, y)
        if matrix[x][y+1] < 9 and [x, y+1] != old_node:  # east is < 9 and not previous node
            basin_mapper(matrix, x, y+1, x, y)
        if matrix[x-1][y] < 9 and [x-1, y] != old_node:  # north is < 9 and not previous node
            basin_mapper(matrix, x-1, y, x, y)
    # left edge case, always 3 neighbors: east south north
    elif 0 < x < len(matrix) - 1 and y == 0:
        if matrix[x][y+1] < 9 and [x, y+1] != old_node:  # east is < 9 and not previous node
            basin_mapper(matrix, x, y+1, x, y)
        if matrix[x+1][y] < 9 and [x+1, y] != old_node:  # south is < 9 and not previous node
            basin_mapper(matrix, x+1, y, x, y)
        if matrix[x-1][y] < 9 and [x-1, y] != old_node:  # north is < 9 and not previous node
            basin_mapper(matrix, x-1, y, x, y)
    # top left corner case, always 2 neighbors: east south
    elif x == 0 and y == 0:
        if matrix[x][y + 1] < 9 and [x, y+1] != old_node:  # east is < 9 and not our previous node
            basin_mapper(matrix, x, y+1, x, y)
        if matrix[x+1][y] < 9 and [x+1, y] != old_node:  # south is < 9 and not previous node
            basin_mapper(matrix, x+1, y, x, y)
    # top right corner case, always 2 neighbors: west south
    elif x == 0 and y == len(matrix[x]) - 1:
        if matrix[x][y-1] < 9 and [x, y-1] != old_node:  # west is below 9 and not our previous node
            basin_mapper(matrix, x, y-1, x, y)
        if matrix[x+1][y] < 9 and [x+1, y] != old_node:  # south is < 9 and not previous node
            basin_mapper(matrix, x+1, y, x, y)
    # bottom left corner case, always 2 neighbors: east north
    elif x == len(matrix) - 1 and y == 0:
        if matrix[x][y+1] < 9 and [x, y+1] != old_node:  # east is < 9 and not previous node
            basin_mapper(matrix, x, y+1, x, y)
        if matrix[x-1][y] < 9 and [x-1, y] != old_node:  # north is < 9 and not previous node
            basin_mapper(matrix, x-1, y, x, y)
    # bottom right corner case, always 2 neighbors: west north
    elif x == len(matrix) - 1 and y == len(matrix[x]) - 1:
        if matrix[x][y-1] < 9 and [x, y-1] != old_node:  # west is below 9 and not our previous node
            basin_mapper(matrix, x, y-1, x, y)
        if matrix[x-1][y] < 9 and [x-1, y] != old_node:  # north is < 9 and not previous node
            basin_mapper(matrix, x-1, y, x, y)
    # x y is our basin low point
    # a function that uses our earlier cases to reverse map every possible path to a nine from origin?
    new_matrix = copy.deepcopy(matrix)
    new_matrix[x][y] = 0
    display_matrix(new_matrix)
    record[f"m:{x},{y}"] = True
    pass


if __name__ == "__main__":
    # display_graph(matrix_map)
    print("part 1: ", iterate_matrix(matrix_map))
    print("part 2: ", iterate_matrix(matrix_map, True))
