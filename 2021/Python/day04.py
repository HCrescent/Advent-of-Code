"""Day 04 Advent_of_Code"""
with open("input/day04.txt", 'r') as infile:
    data = list(infile)
board_dict = {}
raffle = data[0].strip().split(',')
raffle = [int(each) for each in raffle]
data.pop(0)
num = 0
for index in data:
    if data[0] == "\n":
        data.pop(0)
        temp_board = []
        for _ in range(5):
            # to make a temp board before we add it to the dict
            # for 5 lines strip split the strings,
            # i cant int the list unless i use map to take the int function
            # and apply it to each element in the list, but then map returns an object
            # list() the object to turn it back into a list and viola append
            temp_board.append(list(map(int, data[0].strip().split())))
            data.pop(0)
        board_dict[f"board{num}"] = temp_board
        num += 1
# global variables
winning_key = ""
# these two variables are just for making an exception to print the first win and last win
dict_length = len(board_dict)
win_count = 0


def play_bingo(numbers):
    while len(numbers) > 0:
        mark_boards(numbers[0], board_dict)
        while check_for_win(numbers[0]):
            board_dict.pop(winning_key)
        numbers.pop(0)
    return


def mark_boards(call_num, board):
    for board_key in board_dict:
        for row in board[board_key]:
            for i in range(len(row)):
                if row[i] == call_num:
                    row[i] = None
    return


def calc_score(winning_number, board_key):
    score = 0
    for row in board_dict[board_key]:
        for number in row:
            if number is not None:
                score += number
    # we only want to print out the first win and the last win for the puzzle solution
    global win_count
    if win_count == 0:
        print("Part1: ", board_key, " score: ", score * winning_number)
    if win_count == dict_length - 1:
        print("Part2: ", board_key, " score: ", score * winning_number)
    win_count += 1
    # using this global
    global winning_key
    winning_key = board_key


def check_for_win(winning_number):
    # for each board in the dict
    for each in board_dict:
        # for each row in the matrix check for bingo
        for row in board_dict[each]:
            if row.count(None) == 5:
                calc_score(winning_number, each)
                return True
        # for each column in the matrix check for bingo
        for digit in range(len(board_dict[each][0])):
            column = [board_dict[each][i][digit] for i in range(len(board_dict[each]))]
            if column.count(None) == 5:
                calc_score(winning_number, each)
                return True
    return False


if __name__ == "__main__":
    play_bingo(raffle)
