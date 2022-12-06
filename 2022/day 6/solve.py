#/bin/env python3

def read_stream():
    with open("input.txt", "r") as f:
        while True:
            c = f.read(1)

            if c=='\n':
                break

            yield(c)

def pack_word(stream, word_size=4):
    word = []
    for c in stream:
        word.append(c)

        if len(word)==word_size:
            yield(word)
            word.pop(0)

def check_packet(words):
    for word in words:
        yield(len(set(word))==len(word))

def get_packet_index(word_size=4):
    i = 0
    for status in check_packet(pack_word(read_stream(), word_size)):
        if status:
            break
        i+=1
    return i+word_size

print(f"Soution part1 is {get_packet_index(4)}")
print(f"Soution part2 is {get_packet_index(14)}")
