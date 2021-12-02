import sys
import re
import functools
import copy

# http://adventofcode.com/2020/day/22

decks = [[], []]

input()
i = 0
for rawin in sys.stdin:
    rawin = rawin[:-1] # newlinestrip
#    print('"' + rawin + '"')
    if rawin:
        decks[i].append(int(rawin))
#        print(rawin)
    else:
        i += 1
        input()


decks = [deck[::-1] for deck in decks]
print(decks)

def play(card1, card2):
    return (0, [card1, card2]) if card1 > card2 else (1, [card2, card1])

def sum_deck(deck):
    result = 0
    for i, card in enumerate(deck, 1):
        result += i*card
    return result

def mega_sum_deck(deck, base):
    return sum((card-1) * base**i for i, card in enumerate(deck))

def krig(input_deck):
    decks = copy.deepcopy(input_deck)
    holds = [[], []]
    win = False
    i_round = 1
    while True:
        for i, deck in enumerate(decks):
            if len(deck) == 0:
                decks[i] = holds[i][::-1]
                holds[i] = []
                if len(decks[i]) == 0:
                    winner = (i + 1) % 2
                    win = True
        if win:
            winner_deck = holds[winner][::-1] + decks[winner]
#            print(holds[winner], decks[winner], winner_deck)
#            print(mega_sum_deck(holds[winner], decks[winner], max(decks[winner])))
            return winner, sum_deck(winner_deck)
        round_result = play(decks[0].pop(), decks[1].pop())
#        print(i_round, round_result)
        holds[round_result[0]] += round_result[1]
        i_round += 1

def recursive_krig(decks, depth=0):
#    print(depth)
    holds = [[], []]
    max_card = max(max(deck) for deck in decks)
    visited_states = [[mega_sum_deck(deck, max_card)] for deck in decks]
    visited_states = [
            ["".join(str(card) for card in deck)]
         for deck in decks
    ]
    win = False
    i_round = 1
    while True:
        for i, deck in enumerate(decks):
            # Har nogen ikke flere kort?
            if len(deck) == 0:
                decks[i] = holds[i][::-1]
                holds[i] = []
                if len(decks[i]) == 0:
    #                print("Tom stabel")
                    winner = (i + 1) % 2
                    win = True
        # Har begge et tidligere besøgt deck?
#        print(visited_states)
        if all(visited_states[i][-1] in visited_states[i][:-1] for i in range(2)):
#            print("Genbesøg")
            winner = 0
            win = True
        if win:
#            print(decks[winner])
            return winner, sum_deck(decks[winner])
        if all(len(deck) + len(hold) > deck[-1] for deck,hold in zip(decks, holds)):
            # Så kan vi recurse
#            print("Recurse")
            decks = [hold[::-1] + deck for hold, deck in zip(holds, decks)]
            holds = [[],[]]
            indsatser = [deck.pop() for deck in decks] # Spiller 0 venstrest i denne bunke
            recursive_round_result = recursive_krig(
                    [deck[-indsats:] for deck, indsats in zip(decks, indsatser)]
                    ,
                    depth+1
                    )
            round_winner = recursive_round_result[0]
            # round_result skal have vinderens kort *venstrest*
            round_result = (round_winner, indsatser[::-1]) if round_winner else (round_winner, indsatser)
        else:
            round_result = play(decks[0].pop(), decks[1].pop())
        visited_states = [
                state_list + ["".join(str(card) for card in deck)]#[mega_sum_deck(deck, max_card)]
                for state_list, deck in zip(visited_states, decks)
            ]
#        print(i_round, round_result)
        decks[round_result[0]] = round_result[1][::-1] + decks[round_result[0]]
        i_round += 1

print(krig(decks))
print(recursive_krig(decks))
