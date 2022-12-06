"""Day 16 Advent_of_Code 2021"""
with open("input/day16.txt", 'r') as infile:
	data = infile.read().rstrip()
# could use built in int(data, base=16) but I suspect that this would be using a lot more resources
# as it would be calculating the large decimal representation of the integer
# zfill because we want those leading zeros for continuous packet data
# slicing is for omitting the base prefix string
hex_conversion = {hex(i).upper()[2:]: bin(i)[2:].zfill(4) for i in range(16)}


def hex_to_bin(packet):
	return "".join([hex_conversion[char] for char in packet])


def parsePacketBinPart1(binary_string):
	slicer = 6
	ver_sum = int(binary_string[:3], base=2)  # add the version number to the running version sum
	match binary_string[3:6]:  # match the packet type
		case "100":  # case 4 literal value
			build_literal = ""
			while binary_string[slicer] == "1":  # while the first bit in each five is 1
				build_literal += binary_string[slicer+1:slicer+5]
				slicer += 5
			else:  # we hit the first 0 grab the last bits
				build_literal += binary_string[slicer+1:slicer+5]
				pkt_len = slicer+5
				return str(int(build_literal, base=2)), ver_sum, pkt_len  # return literal value, and the running version sum
		case _:  # operator packet
			instruction_string = ""  # ultimately we will build a string of the required operations and literals
			match binary_string[slicer]:  # check the Length Type ID
				case "0":  # next 15 bits indicate length of bits of sub-packets
					subPacket_bit_endpoint = int(binary_string[slicer+1:slicer+16], base=2) + slicer + 16
					packet_i = slicer+16
					while packet_i < subPacket_bit_endpoint:
						tmp_literal, tmp_vSum, pkt_delta = parsePacketBinPart1(binary_string[packet_i:])
						instruction_string += " " + tmp_literal  # build the instruction string
						ver_sum += tmp_vSum  # update teh version sum for part 1
						packet_i += pkt_delta  # the next pkt index is updated by the length of the previous pkt
					return instruction_string, ver_sum, packet_i
				case '1':  # next 11 bits indicate total number of sub-packets
					total_subPackets = int(binary_string[slicer+1:slicer+12], base=2)
					packet_i = slicer+12  # indexer for start of packet
					for _ in range(total_subPackets):  # for each sub-packet
						tmp_literal, tmp_vSum, pkt_delta = parsePacketBinPart1(binary_string[packet_i:])
						instruction_string += " " + tmp_literal  # build the instruction string
						ver_sum += tmp_vSum  # update teh version sum for part 1
						packet_i += pkt_delta  # the next pkt index is updated by the length of the previous pkt
					return instruction_string, ver_sum, packet_i


if __name__ == "__main__":
	print(data)
	print(hex_to_bin(data))
	print("part 1: ", parsePacketBinPart1(hex_to_bin(data))[-2])
	# print("part 2: ")
