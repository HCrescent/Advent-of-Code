"""Day 05 Advent_of_Code"""
# SLOPE FORMULA m=(y2-y1)/(x2-x1)
with open("input/day05.txt", 'r') as infile:
    data = [line.replace(" -> ", ',').rstrip() for line in infile]
    data2 = []
    for i in range(len(data)):
        data2.append(list(map(int, data[i].strip().split(','))))
x1 = [data2[_][0] for _ in range(len(data2))]
y1 = [data2[_][1] for _ in range(len(data2))]
x2 = [data2[_][2] for _ in range(len(data2))]
y2 = [data2[_][3] for _ in range(len(data2))]


def display_graph(graph):
    for _ in range(len(graph)):
        print(graph[_])


def create_grid(bound):
    graph = [[0 for _ in range(bound)] for _ in range(bound)]
    return graph


def count_dots(matrix):
    overlap_dots = 0
    for _ in range(len(matrix)):
        for i in range(len(matrix)):
            if matrix[_][i] > 1:
                overlap_dots += 1
    return overlap_dots


def get_slope(x1, x2, y1, y2):
    if y2 - y1 == 0:
        return 0  # horizontal line
    if x2 - x1 == 0:
        return None  # vertical line
    # no partial slops so no need for floats or fractions
    slope = (y2-y1) // (x2-x1)
    return slope


def plot_line(matrix, slope, x1, x2, y1, y2):
    """Takes the slope, and two points, plots the line on the lattice.
    # Each slope loop contains a check to see which point is

    :param matrix: list of list - The big one
    :param slope: slop of the line of two points x1,y1 x2,y2
    :param x1: int
    :param x2: int
    :param y1: int
    :param y2: int
    :return:
    """

    if slope == 0:  # horizontal line increase x value
        for i in range(abs(x1-x2)+1):
            if x1 < x2:
                matrix[x1+i][y1] += 1
            if x2 < x1:
                matrix[x2+i][y1] += 1
    if slope is None:  # vertical line increase y value
        for i in range(abs(y1-y2)+1):
            if y1 < y2:
                matrix[x1][y1+i] += 1
            if y2 < y1:
                matrix[x1][y2+i] += 1
    if slope == -1:  # negative slope x and y are inversely related so we have a -i in each option
        for i in range(abs(x1-x2)+1):
            if x1 < x2:
                matrix[x1+i][y1-i] += 1
            if x2 < x1:
                matrix[x1-i][y1+i] += 1
    if slope == 1:  # positive slope
        for i in range(abs(x2-x1)+1):
            if x1 < x2:
                matrix[x1+i][y1+i] += 1
            if x2 < x1:
                matrix[x2+i][y2+i] += 1
    return


def plot_lattice_points_part1(matrix, x1, x2, y1, y2):
    """Takes the Empty plot matrix and all coordinates, and plots points where lines are 0 or no slope.
    # only plots the vertical/horizontal lines for part 1

    :param matrix: list of lists - The big one
    :param x1: list
    :param x2: list
    :param y1: list
    :param y2: list
    :return:
    """
    # for each line data
    for _ in range(len(x1)):
        slope = get_slope(x1[_], x2[_], y1[_], y2[_])
        if slope == 0:  # horizontal line
            plot_line(matrix, slope, x1[_], x2[_], y1[_], y2[_])
        if slope is None:  # vertical line
            plot_line(matrix, slope, x1[_], x2[_], y1[_], y2[_])
    return


def plot_lattice_points(matrix, x1, x2, y1, y2):
    """Takes the Empty plot matrix and all coordinates, and plots points where lines intersect lattice.

    :param matrix: list of lists - The big one
    :param x1: list
    :param x2: list
    :param y1: list
    :param y2: list
    :return:
    """
    # for each line data
    for _ in range(len(x1)):
        slope = get_slope(x1[_], x2[_], y1[_], y2[_])
        if slope == 0:  # horizontal line
            plot_line(matrix, slope, x1[_], x2[_], y1[_], y2[_])
        if slope is None:  # vertical line
            plot_line(matrix, slope, x1[_], x2[_], y1[_], y2[_])
        if slope == 1 or slope == -1:
            plot_line(matrix, slope, x1[_], x2[_], y1[_], y2[_])
    return


if __name__ == "__main__":
    grid_range = list(map(max, [list(map(max, data2))]))
    # remember +1 because we include ZERO FOR THE ORIGIN :)
    matrix_monarch = create_grid(grid_range[0]+1)
    plot_lattice_points_part1(matrix_monarch, x1, x2, y1, y2)
    print("part 1: ", count_dots(matrix_monarch))
    matrix_monarch = create_grid(grid_range[0]+1)
    plot_lattice_points(matrix_monarch, x1, x2, y1, y2)
    print("part 2: ", count_dots(matrix_monarch))
