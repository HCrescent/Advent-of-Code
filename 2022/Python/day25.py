"""Day 25 Advent_of_Code 2022"""
bal_quin = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
bal_quin_inv = {2: '2', 1: '1', 0: '0', -1: '-', -2: '='}
with open("input/day25.txt", 'r') as infile:
	data = [[bal_quin[char] for char in line.rstrip()] for line in infile]


def balancedToDecimal(number, base):
	""" converts a balanced base number to decimal

	:param number: List - list of integers of the balanced number, ex: balanced ternary [1, 0, -1]
	:param base: Int - balanced int, must be odd for balanced base systems to be balanced
	:return: Int - decimal conversion
	"""
	mag = 0
	decimal = 0
	while number:
		decimal += number.pop() * base**mag
		mag += 1
	return decimal


def decimalToBase(number, base):
	# converts decimal integer to simple small bases
	base_str = ""
	while number:
		base_str += str(number % base)
		number //= base
	return base_str[::-1]


def decimalToBalancedBase(number, base=5):
	base_str = []
	while number:  # while number is not 0
		remainder = number % base
		if remainder < (base//2)+1:  # if the remainder is below the digit upperbound for the base
			base_str.append(remainder)
			number //= base
			continue
		tmp_quotient = (number // base) + 1
		base_str.append(number - (tmp_quotient * base))
		number = tmp_quotient
	return base_str[::-1]


def part1():
	# first gets the decimal total for all balanced quinary inputs then converts the answer back into balanced quinary
	decimal_data = [balancedToDecimal(line, 5) for line in data]
	total = sum(decimal_data)
	balanced_quinary = decimalToBalancedBase(total)
	bal_str = "".join([bal_quin_inv[char] for char in balanced_quinary])
	return bal_str


if __name__ == "__main__":
	print("part 1: ", part1())
	# print("part 2: ")
