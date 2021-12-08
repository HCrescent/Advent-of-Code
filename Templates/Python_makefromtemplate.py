"""Create new files for an advent of code problem in Project Repo"""
import urllib.request
import os.path


def create_files(year, day):
    if urllib.request.urlopen(f"https://adventofcode.com/{year}/day/{day}").getcode() == 200:
        if int(day) < 10:
            day = str(int(day))
            day = "0" + day
        if not os.path.exists(f"../{year}/Python/day{day}.py"):
            with open(f"../{year}/Python/day{day}.py", 'w') as new_file:
                new_file.write(f"\"\"\"Day {day} Advent_of_Code\"\"\""
                              f"\n"
                              f"\n"
                              f"\n"
                              f"\n"
                              f"\n"
                              f"\n"
                              f"\n")
            if not os.path.exists(f"../{year}/Python/input/day{day}.txt"):
                with open(f"../{year}/Python/input/day{day}.txt", 'w') as new_input:
                    new_input.write("insert input here")
            return
        print("exists")
        return
    print("error opening site")
    return


if __name__ == "__main__":
    create_files(input("year: "), input("day: "))
