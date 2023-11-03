# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

import numpy
import scipy

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

def simulate_verdict(p1, p2):
    count = 0
    while True:
        if count > 10000:
            return "draw"
        card1 = p1.pop(0)
        card2 = p2.pop(0)
        card1_value = cards.index(card1)
        card2_value = cards.index(card2)
        if card1_value > card2_value:
            p1.append(card2)
            if len(p2) == 0:
                return "player 1"
        elif card2_value > card1_value:
            p2.append(card1)
            if len(p1) == 0:
                return "player 2"
        else:
            p1.append(card1)
            p2.append(card2)
        count += 1


n = int(input())
verdicts = []
for i in range(n):
    player_one = input().split(" ")
    player_two = input().split(" ")
    verdicts.append(simulate_verdict(player_one, player_two))

for verdict in verdicts:
    print(verdict)