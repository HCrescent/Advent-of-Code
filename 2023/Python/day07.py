"""Day 07 Advent_of_Code 2023"""
with open("input/day07.txt", 'r') as infile:
	data = [line.rstrip() for line in infile]

card_scores = {str(_): _ for _ in range(2, 10)}
card_scores.update({'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14})
hand_names = ["High Card", "One Pair", "Two Pairs", "Three of a Kind", "Full House",
			  "Four of a Kind", "Five of a Kind"]
hand_scores = {name: i for i, name in enumerate(hand_names)}


class CamelHand:
	def __init__(self, hand):
		self.cards, self.bid = hand.split()
		self.bid = int(self.bid)
		self.hand_type = evalHandType(self.cards)
		self.hand_score = hand_scores[self.hand_type]

	def winByHighCard(self, other):
		for i, value in enumerate(self.cards):
			if value == other.cards[i]:
				continue
			return card_scores[value] < card_scores[other.cards[i]]


	def part2(self):
		match self.hand_score:
			case 0:  # high card -> one pair
				self.hand_score = hand_scores["One Pair"]
			case 1:  # one pair -> three of a kind
				self.hand_score = hand_scores["Three of a Kind"]
			case 2:  # two pair -> full house
				j_count = self.cards.count('J')
				if j_count == 1:
					self.hand_score = hand_scores["Full House"]
				else:
					self.hand_score = hand_scores["Four of a Kind"]
			case 3:  # three of a kind -> four of a kind
				self.hand_score = hand_scores["Four of a Kind"]
			case 4:  # full house -> five of a kind
				self.hand_score = hand_scores["Five of a Kind"]
			case 5:  # four of a kind -> five of a kind
				self.hand_score = hand_scores["Five of a Kind"]
		return

	def __lt__(self, other):
		if self.hand_score != other.hand_score:
			return self.hand_score < other.hand_score
		else:
			return self.winByHighCard(other)

	def __rmul__(self, other):
		if type(other) == int:
			return other * self.bid

	def __repr__(self):
		return f"{self.cards}, {self.hand_type}, {self.hand_score}, {self.bid}/"


def evalHandType(hand):
	# start with checking the length of the set of numbers for each hand
	unique_values = len({card for card in hand})
	match unique_values:
		# only 2 different numbers means hands must be Four of a Kind or Full House
		case 2:
			# if any of the values have counts greater than 3 it's a Four of a Kind, if not it's a Full House
			hand_values_list = [card[0] for card in hand]
			for value in hand_values_list:
				if hand_values_list.count(value) > 3:
					return "Four of a Kind"
			else:
				return "Full House"
		# only 3 different numbers means possibilities are Three of a Kind or Two Pairs
		case 3:
			# if any of the values have counts greater than 2, it's a Three of a Kind, if not it's Two Pairs
			hand_values_list = [card[0] for card in hand]
			for value in hand_values_list:
				if hand_values_list.count(value) > 2:
					return "Three of a Kind"
			else:
				return "Two Pairs"
		case 4:
			return "One Pair"
		case 5:
			return "High Card"
		case _:
			return "Five of a Kind"


def part1(part2=False):
	camel_hands = [CamelHand(each) for each in data]
	if part2:
		card_scores.update({'J': 1})
		for each in camel_hands:
			if 'J' in each.cards:
				each.part2()
	camel_hands.sort()
	total = 0
	for i, each in enumerate(camel_hands):
		total += (i+1) * each
	return total


if __name__ == "__main__":
	print("part 1: ", part1())
	print("part 2: ", part1(True))
