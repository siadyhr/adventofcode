import sys
import re
import functools
import copy

# http://adventofcode.com/2020/day/23

#cups = {i : int(x) for i, x in enumerate(input())}
cups = [int(x) for  x in input()]
print(cups)
print()

def move(cups, current_cup_index):
    free_cups = [
            cups[(current_cup_index+i) % len(cups)] for i in range(1,4)
    ]
    remaining_cups = [cup for cup in cups if cup not in free_cups]
    i = 1
    while True:
        destination_cup = 1 + (cups[current_cup_index]-i-1)%9
        if destination_cup not in free_cups:
            break
        i += 1
    destination_cup_index = remaining_cups.index(destination_cup)
#    print("\t", remaining_cups)
#    print("\t", free_cups)
#    print("\t", destination_cup_index, destination_cup)
    new_cups = (
            remaining_cups[:destination_cup_index+1]
            +
            free_cups
            +
            remaining_cups[destination_cup_index+1:]
            )
    return new_cups, (new_cups.index(cups[current_cup_index])+1)%9

def get_nthbour(cups, current_cup, n):
    result = current_cup
    for _ in range(n+1):
        result = cups[result]
    return result

def move_new(cups, current_cup):
    # Lav hånd
    hand = [cups[current_cup]]
    for _ in range(2):
        hand.append(cups[hand[-1]])
    # Fjern hånden ved at lime på begge sider
    cups[current_cup] = get_nthbour(cups, current_cup, 3)
    destination_cup = ((current_cup - 2) % len(cups)) + 1
    while destination_cup in hand:
        destination_cup = ((destination_cup - 2) % len(cups)) + 1
    # Lim hånd på destination+1
    cups[hand[-1]] = cups[destination_cup]
    # Lim destination på hånd
    cups[destination_cup] = hand[0]
    return cups, cups[current_cup]


def play_cups(cups, time):
    new_cups, index = cups, 0
    for _ in range(time):
    #    print(new_cups, index%len(cups), new_cups[index%len(cups)])
        new_cups, index = move(new_cups, index%len(cups))
    return new_cups

def play_cups_new(cups, current_cup, time):
    for _ in range(time):
        if _%100000 == 0:
            print(_/10000000)
    #    print(new_cups, index%len(cups), new_cups[index%len(cups)])
        cups, current_cup = move_new(cups, current_cup)
    return cups


def parse_cups_1(cups):
    index = cups.index(cups[(cups.index(1) + 1)% 9])
    return "".join(str(x) for x in cups[index:] + cups[:index])
    # Der står 1 til sidst - det skal vi IKKE give til aoc

def parse_cups_1_new(cups):
    out = ""
    num = 1
    for _ in range(len(cups)):
        num = cups[num]
        out += str(num)
    return out


#print(parse_cups_1(play_cups(cups, 100)))
fancy_cups = { cup : cup_right for cup, cup_right in zip(cups, cups[1:] + [cups[0]]) }
print(fancy_cups)
result1 = play_cups_new(fancy_cups, cups[0], 100)
print(parse_cups_1_new(result1))

new_cups = cups + list(range(len(cups)+1, 1000001))
new_fancy_cups = { cup : cup_right for cup, cup_right in zip(new_cups, new_cups[1:] + [new_cups[0]]) }
result_cups = play_cups_new(new_fancy_cups, cups[0], 10000000)
right1 = result_cups[1]
right2 = result_cups[right1]
print(right1, right2, right1*right2)
