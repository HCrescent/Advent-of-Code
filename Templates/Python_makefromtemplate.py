"""Create new files for an advent of code problem in Project Repo"""
import urllib.request
from urllib.error import HTTPError
from os import makedirs
import os.path
from os.path import isdir


def create_files(year, day):
    day = str(int(day))
    try:
        assert urllib.request.urlopen(f"https://adventofcode.com/{year}/day/{day}").getcode() == 200
    except HTTPError:
        print("AoC website did not return data at your year/day combination")
        return
    if int(day) < 10:
        day = "0" + day
    path = f"../{year}/Python/input/"
    script_path = f"../{year}/Python/day{day}.py"
    input_path = f"../{year}/Python/input/day{day}.txt"
    if not isdir(path):
        print("Path folders don't yet exist.")
        makedirs(path)
        print("Directories created.")
    if not os.path.exists(script_path):
        with open(script_path, 'w') as new_file:
            new_file.write(f"\"\"\"Day {day} Advent_of_Code {year}\"\"\"\n"
                           f"with open(\"input/day{day}.txt\", 'r') as infile:\n"
                           f"\tdata = list(infile)\n"
                           f"\n"
                           f"\n"
                           f"def fun():\n"
                           f"\tpass\n"
                           f"\n"
                           f"\n"
                           f"if __name__ == \"__main__\":\n"
                           f"\tprint(fun())\n"
                           f"# print(\"part 1: \")\n"
                           f"# print(\"part 2: \")\n")
            print(f"Script day{day}.py created.")
        if not os.path.exists(input_path):
            with open(input_path, 'w') as new_input:
                new_input.write("insert input here")
            print(f"Input input{day}.txt created.")
        return
    print("files already exist")
    return


if __name__ == "__main__":
    create_files(input("year: "), input("day: "))
