"""Day 13 Advent_of_Code 2021"""
with open("input/day13.txt", 'r') as infile:
    data = list(infile)
COORDINATES = []
while data[0] != '\n':
    COORDINATES.append(list(map(int, data.pop(0).rstrip().split(','))))
data.pop(0)
INSTRUCTIONS = [data[_].rstrip() for _ in range(len(data))]


def get_plot_ranges(coordinates):
    x_max = (max([coordinates[_][0] for _ in range(len(coordinates))]))
    y_max = (max([coordinates[_][1] for _ in range(len(coordinates))]))
    return x_max, y_max


def display_graph(graph):
    for i in range(len(graph[0])):
        flipped_list = [graph[_][i] for _ in range(len(graph))]
        print("".join(flipped_list))
    return


def create_matrix(coordinates, line=None, orientation=None, matrix=None):
    x_max, y_max = get_plot_ranges(coordinates)
    match orientation:
        case 'y':
            matrix = plot_points([['.' for _ in range(line)] for _ in range(len(matrix))], coordinates)
        case 'x':
            matrix = plot_points([['.' for _ in range(len(matrix[0]))] for _ in range(line)], coordinates)
        case _:
            matrix = plot_points([['.' for _ in range(y_max + 1)] for _ in range(x_max + 1)], coordinates)
    return matrix


def plot_points(matrix, coordinates):
    for each in coordinates:
        matrix[each[0]][each[1]] = '#'
    return matrix


def fold_horizontal(matrix, line):  # fold along y=
    points = []
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == '#':
                if y < line:
                    points.append([x, y])
                else:
                    points.append([x, line - abs(line-y)])
    folded_matrix = create_matrix(points, line, 'y', matrix)
    return folded_matrix


def fold_vertical(matrix, line):  # fold along x=
    points = []
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == '#':
                if x < line:
                    points.append([x, y])
                else:
                    points.append([line - abs(line - x), y])
    folded_matrix = create_matrix(points, line, 'x', matrix)
    return folded_matrix


def count_dots(matrix):
    count = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == '#':
                count += 1
    return count


def instructions(matrix, folding_instructions):
    for each in folding_instructions:
        number = int(each.split('=')[1])
        if 'x' in each:
            matrix = fold_vertical(matrix, number)
        else:
            matrix = fold_horizontal(matrix, number)
        if folding_instructions.index(each) == 0:
            print("part 1: ", count_dots(matrix))
    return matrix


if __name__ == "__main__":
    paper = create_matrix(COORDINATES)
    paper = instructions(paper, INSTRUCTIONS)
    print("part 2: ")
    display_graph(paper)
