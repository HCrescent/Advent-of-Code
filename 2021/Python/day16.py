"""Day 16 Advent_of_Code 2021"""
with open("input/day16.txt", 'r') as infile:
	data = infile.read().rstrip()
# could use built in int(data, base=16) but I suspect that this would be using a lot more resources
# as it would be calculating the large decimal representation of the integer
# zfill because we want those leading zeros for continuous packet data
# slicing is for omitting the base prefix string
hex_conversion = {hex(i).upper()[2:]: bin(i)[2:].zfill(4) for i in range(16)}


def product(values):
	"""Takes an iterable and creates a product of each element in the iterable

	:param values: List - (or other compatible iterable) to get the product of all elements
	:return: Int - Calculated product
	"""
	prod = 1
	for _ in values:
		prod *= _
	return prod


def hex_to_bin(packet):
	return "".join([hex_conversion[char] for char in packet])


def parsePacketBin(binary_string):
	""" recursive packet interpreter

	:param binary_string: Str - binary data to be processed based on packet structure
	:return: Tuple - (Int, Int, Int) - (evaluated expression result, version sum, packet index)
	"""
	slicer = 6
	ver_sum = int(binary_string[:3], base=2)  # add the version number to the running version sum
	packet_type = binary_string[3:6]
	match packet_type:  # match the packet type
		case "100":  # case 4 literal value
			build_literal = ""
			while binary_string[slicer] == "1":  # while the first bit in each five is 1
				build_literal += binary_string[slicer+1:slicer+5]
				slicer += 5
			else:  # we hit the first 0 grab the last bits
				build_literal += binary_string[slicer+1:slicer+5]
				pkt_len = slicer+5
				return int(build_literal, base=2), ver_sum, pkt_len  # return literal value, running sum, packet length
		case _:  # operator packet
			literal_list = []  # for storing our literals for our operators
			match binary_string[slicer]:  # check the Length Type ID
				case "0":  # next 15 bits indicate length of bits of sub-packets
					subPacket_bit_endpoint = int(binary_string[slicer+1:slicer+16], base=2) + slicer + 16
					packet_i = slicer+16
					while packet_i < subPacket_bit_endpoint:  # until we reach end of sub-packets
						tmp_literal, tmp_vSum, pkt_delta = parsePacketBin(binary_string[packet_i:])
						literal_list.append(tmp_literal)  # add literal to list for processing
						ver_sum += tmp_vSum  # update the version sum for part 1
						packet_i += pkt_delta  # the next pkt index is updated by the length of the previous pkt
				case _:  # next 11 bits indicate total number of sub-packets
					total_subPackets = int(binary_string[slicer+1:slicer+12], base=2)
					packet_i = slicer+12  # indexer for start of packet
					for _ in range(total_subPackets):  # for each sub-packet
						tmp_literal, tmp_vSum, pkt_delta = parsePacketBin(binary_string[packet_i:])
						literal_list.append(tmp_literal)  # add literal to list for processing
						ver_sum += tmp_vSum  # update the version sum for part 1
						packet_i += pkt_delta  # the next pkt index is updated by the length of the previous pkt
			match packet_type:
				case "000":  # sum packet
					new_literal = sum(literal_list)
				case "001":  # product packet
					new_literal = product(literal_list)
				case "010":  # min packet
					new_literal = min(literal_list)
				case "011":  # max packet
					new_literal = max(literal_list)
				case "101":  # greater than packet
					new_literal = int(literal_list[0] > literal_list[1])
				case "110":  # less than packet
					new_literal = int(literal_list[0] < literal_list[1])
				case "111":  # equal packet
					new_literal = int(literal_list[0] == literal_list[1])
			# no case _ because we would re-catch 100 for literals
			# noinspection PyUnboundLocalVariable
			return new_literal, ver_sum, packet_i


if __name__ == "__main__":
	print("part 1: ", parsePacketBin(hex_to_bin(data))[1])
	print("part 2: ", parsePacketBin(hex_to_bin(data))[0])
