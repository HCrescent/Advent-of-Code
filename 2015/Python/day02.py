"""Day 02 Advent_of_Code 2015"""
with open("input/day02.txt", 'r') as infile:
	data = [sorted(list(map(int, line.rstrip().split('x')))) for line in infile]


def sum_calc(dimension_list):
	paper_total = 0
	ribbon_total = 0
	for n in dimension_list:
		paper_total += int(2*(1.5*n[0]*n[1] + n[0]*n[2] + n[1]*n[2]))
		ribbon_total += 2*(n[0] + n[1])
		ribbon_total += (n[0]*n[1]*n[2])
	return ribbon_total, paper_total


if __name__ == "__main__":
	ribbon_len, paper_area = sum_calc(data)
	print("part 1: ", paper_area)
	print("part 2: ", ribbon_len)
