import re
from bitstring import ConstBitStream

f = open("input.txt", "r")
lines = f.read().split('\n')
lines.remove('') 
f.close()

bitstream = ConstBitStream('0x' + lines[0])

def process_packet(bits, stack):
    pos = bits.pos
    version = bits.read('uint:3')
    type = bits.read('uint:3')
    #print("New Packet {}:{} at {}".format(version, type, pos))
    length = 6
    if type == 4:
        final = 1
        val = 0
        while final == 1:
            final = bits.read('uint:1')
            val = (val << 4) + bits.read('uint:4')
            length += 5
        stack.append(val)
        #print("litteral {} on {} bits".format(val, length-6))
    else:
        length_type_id = bits.read('uint:1')
        if length_type_id == 0:
            length += 16
            packet_length = bits.read('uint:15')
            sub_length = 0
            sub_packet_count = 0
            while sub_length < packet_length:
                #print('Sub Packet length: {} {}'.format(sub_length, packet_length))
                l,v = process_packet(bits, stack)
                sub_length += l
                version += v
                sub_packet_count += 1
            length += packet_length
        else:
            length += 12
            sub_packet_count = bits.read('uint:11')
            for c in range(sub_packet_count):
                #print('Sub Packet Idx {} {}'.format(c, sub_packet_count))
                l,v = process_packet(bits, stack)
                length += l
                version += v

        if type == 0:
            val = 0
            for c in range(sub_packet_count):
                val += stack.pop()
        elif type == 1:
            val = 1
            for c in range(sub_packet_count):
                val *= stack.pop()
        elif type == 2:
            val = stack.pop()
            for c in range(sub_packet_count-1):
                val = min(val, stack.pop())
        elif type == 3:
            val = stack.pop()
            for c in range(sub_packet_count-1):
                val = max(val, stack.pop())
        elif type == 5:
            a = stack.pop()
            b = stack.pop()
            val = 1 if a < b else 0
        elif type == 6:
            a = stack.pop()
            b = stack.pop()
            val = 1 if a > b else 0
        elif type == 7:
            a = stack.pop()
            b = stack.pop()
            val = 1 if a == b else 0
        else:
            print("Invalid CMD {}".format(type))

        stack.append(val)
        
    return length, version

stack = []
length, version = process_packet(bitstream, stack)
#print(stack)
    
print("Solution part1 is {}".format(version))
print("Solution part2 is {}".format(stack.pop()))
