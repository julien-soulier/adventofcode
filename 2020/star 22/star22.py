import re
import string
import math

f = open("input.txt", "r")
lines = f.read().split('\n')
f.close()


deck = {}
players = []
game_history = {}

def init_deck():
    player = ''
    for line in lines:
        if len(line)==0:
            player=''
            continue
        
        if player=='':
            player = line[0:-1]
            deck[player] = []
            players.append(player)
        else:
            deck[player].append(int(line))

def game_end(deck):
    for player in deck.keys():
        if len(deck[player])==0:
            return True
    return False

def get_winner(deck):
    for player in deck.keys():
        if len(deck[player])>0:
            return player
    return None

def play_round():
    card={}
    for player in deck.keys():
        card[player] = deck[player].pop(0)
    winner = max(card, key=card.get)
    deck[winner].append(max(card.values()))
    deck[winner].append(min(card.values()))

def play_recursive_round(deck, recursion):
    #print("New round #{} {} - {}".format(recursion, len(deck['Player 1']), len(deck['Player 2'])))

    card={}
    do_recurse = True
    for player in deck.keys():
        card[player] = deck[player].pop(0)
        if card[player] > len(deck[player]):
            do_recurse = False
    if do_recurse:
        deck_copy = {}
        for player in deck.keys():
            c = card[player]
            deck_copy[player] = deck[player][0:c].copy() 
        winner = play_recursive_game(deck_copy, recursion+1)
    else:   
        winner = max(card, key=card.get)
    deck[winner].append(card[winner])
    winner_idx = players.index(winner)
    loser_idx = 1 - winner_idx
    loser = players[loser_idx]
    deck[winner].append(card[loser])

def get_score(player):
    score = 0
    val = len(deck[player])
    for card in deck[player]:
        score += card * val
        val -=1
    return score

def play_normal_game():
    init_deck()
    while not game_end(deck):
        play_round()

    print(deck)
    return get_score(get_winner(deck))

def get_game_key(deck):
    game_key = ''
    for player in deck.keys():
        game_key += ','.join(list(map(str, deck[player])))
    return game_key

def play_recursive_game(deck, recursion):
    game_history[recursion] = []

#    print("entering recursive game #{} {} - {}".format(recursion, len(deck['Player 1']), len(deck['Player 2'])))
    while not game_end(deck):
        game_key = get_game_key(deck)
        if game_key in game_history[recursion]:
#            print('FOUND RECURSION')
#            print("Finishing recursive game #{}: {}".format(recursion, players[0]))
            return players[0]
        else:
            game_history[recursion].append(game_key)
        play_recursive_round(deck, recursion)
#    print("Finishing recursive game #{}: {}".format(recursion, get_winner(deck)))
    
    return get_winner(deck)

res1=play_normal_game()
print("solution part 1: {}".format(res1))
    
init_deck()
print(deck)
winner=play_recursive_game(deck, 0)
print("player {} won".format(winner))
res2 = get_score(winner)
print("solution part 2: {}".format(res2))