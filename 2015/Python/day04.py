"""Day 04 Advent_of_Code 2015"""
import hashlib
with open("input/day04.txt", 'r') as infile:
	data = infile.read().rstrip()


def find_leading_z(zeros, in_str=data):
	num = 1
	match_str = "".zfill(zeros)
	while True:
		if hashlib.md5(f"{in_str}{num}".encode()).hexdigest()[0:zeros] == match_str:
			break
		num += 1
	return num


if __name__ == "__main__":
	print("part 1: ", find_leading_z(5))
	print("part 2: ", find_leading_z(6))
