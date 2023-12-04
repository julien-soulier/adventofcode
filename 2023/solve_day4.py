#!/bin/env python3

import re

def get_pile_len(fname):
    with open(fname, "r") as f:
        return sum(1 for line in f)

def get_numbers_set(numbers_str):
    return set(re.findall(r'\d+', numbers_str))

def process_cards(fname):
    with open(fname, "r") as f:
        for l in f:
            cards = l.split(":")
            tokens = cards[1].split("|")
            winning_set = get_numbers_set(tokens[0])
            numbers_set = get_numbers_set(tokens[1])
            winning = winning_set.intersection(numbers_set)
            yield len(winning)

def process_input(fname="input_4.txt", part=1):
    card_cnt = [1] * get_pile_len(fname)
    card_idx=0
    for win_cnt in process_cards(fname):
        if part==1:
            yield 0 if win_cnt == 0 else 2**(win_cnt-1)
        else:
            for i in range(card_idx+1, card_idx+1+win_cnt):
                card_cnt[i] += card_cnt[card_idx]
            yield card_cnt[card_idx]

        card_idx += 1

print(f"The solution for part1 is {sum(process_input(part=1))}")
print(f"The solution for part2 is {sum(process_input(part=2))}")
    