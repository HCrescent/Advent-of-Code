"""Create new files for an advent of code problem in Project Repo"""
import sqlite3
import urllib.request
from urllib.error import HTTPError
from os import makedirs
import os.path
from os.path import isdir


def create_files(year, day):
    """ Takes a year and day input and generates files in the repository for ease of setting up new work.

    :param year: Str - string for the year in 4 digit form
    :param day: Str -
    :return: None
    """
    # remove potential leading 0s in input string
    year = str(int(year))
    day = str(int(day))
    site_path = f"https://adventofcode.com/{year}/day/{day}"
    try:
        assert urllib.request.urlopen(f"{site_path}").getcode() == 200
    except HTTPError:
        print("AoC website did not return data at your year/day combination")
        return
    two_digit_day = day.zfill(2)
    path = f"../{year}/Python/input/"
    script_path = f"../{year}/Python/day{two_digit_day}.py"
    input_path = f"../{year}/Python/input/day{two_digit_day}.txt"
    # if we haven't created that folder structure for the existing year of problems
    if not isdir(path):
        print("Path folders don't yet exist.")
        makedirs(path)
        print("Directories created.")
    # if the script doesnt already exist, create it
    if not os.path.exists(script_path):
        with open(script_path, 'w') as new_file:
            new_file.write(f"\"\"\"Day {two_digit_day} Advent_of_Code {year}\"\"\"\n"
                           f"with open(\"input/day{two_digit_day}.txt\", 'r') as infile:\n"
                           f"\tdata = [line for line in infile]\n"
                           f"\n"
                           f"\n"
                           f"def fun():\n"
                           f"\tpass\n"
                           f"\n"
                           f"\n"
                           f"if __name__ == \"__main__\":\n"
                           f"\tprint(fun())\n"
                           f"\t# print(\"part 1: \")\n"
                           f"\t# print(\"part 2: \")\n")
            print(f"Script day{two_digit_day}.py created.")
    # if script's input doesnt exist yet, get session cookie and request data
    if not os.path.exists(input_path):
        # set up required session cookie
        # get my personal path data without pasting it in an extra file or statically in the script
        # if you want to use this script you'll have to know where your own files are and edit this
        appdata = os.getenv("APPDATA")
        profile = os.listdir(f"{appdata}\\Mozilla\\Firefox\\Profiles")[1]
        cookies_path = f"{appdata}\\Mozilla\\Firefox\\Profiles\\{profile}\\cookies.sqlite"
        db = sqlite3.connect(f"file:{cookies_path}?mode=ro", uri=True)
        query = "SELECT value FROM moz_cookies WHERE host=\".adventofcode.com\" AND name=\"session\";"
        # grabbing the string
        session = "session=" + db.cursor().execute(query).fetchone()[0]
        # make a Request object with urllib library so we can add our session cookie into urlopen request
        input_request = urllib.request.Request(f"{site_path}/input")
        input_request.add_header("Cookie", session)
        # try to grab input text
        try:
            urllib.request.urlopen(input_request).getcode() == 200
        except HTTPError:
            print("Something went wrong grabbing text file, could not get HTTP code 200.")
            return
        # start writing new file with input data
        with open(input_path, 'w') as new_input:
            new_input.writelines(line.decode('utf-8') for line in urllib.request.urlopen(input_request))
        print(f"Input input{day}.txt created.")
        return
    print("files already exist")
    return


if __name__ == "__main__":
    create_files(input("year: "), input("day: "))
