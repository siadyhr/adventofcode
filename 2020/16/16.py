import sys
import re
import functools
import copy

# http://adventofcode.com/2020/day/16

# Keys
keys = {}
for rawin in sys.stdin:
    rawin = rawin[:-1] # newlinestrip
#    print('"' + rawin + '"')
    if rawin:
        rawin = rawin.split(":")
        ranges = [
                [int(num) for num in pair.split("-")]
                for pair in rawin[1].split(" ")[1::2]
        ]

        keys[rawin[0]] = ranges
#        print(rawin)
    else:
        break
# My ticket
input()
myticket = [int(x) for x in input().split(",")]
input()
input()
# Other tickets
tickets = []
for rawin in sys.stdin:
    rawin = rawin[:-1] # newlinestrip
#    print('"' + rawin + '"')
    if rawin:
        tickets.append([
            int(num) for num in rawin.split(",")
        ])
    else:
        pass

def get_invalids(ticket, part=2):
    invalids = []
    for num in ticket:
        good = False
        for rule in keys.values():
            if (rule[0][0] <= num <= rule[0][1] or rule[1][0] <= num <= rule[1][1]):
                good = True
                break
        if good:
            continue
        invalids.append(num)

    if part == 1:
        return set(invalids)
    if not invalids:
        return ticket

# Del 1
#invalid_nums = ([sum(get_invalids(ticket, 1)) for ticket in tickets])
#print(invalid_nums)

valid_tickets_tmp = [get_invalids(ticket, 2) for ticket in tickets]
valid_tickets = [ticket for ticket in valid_tickets_tmp if ticket is not None]
#print(valid_tickets)
def restore_keys(keys, tickets):
    restored_key_candidates = {}
    for pos, values in enumerate((zip(*tickets))):
        for pair in keys.items():
            good = False
            for value in values:
                if pair[1][0][0] <= value <= pair[1][0][1] or pair[1][1][0] <= value <= pair[1][1][1]:
                    good = True
                    continue # Næste value
                good = False
                break # Stop values, næste nøgle
            if not good:
                continue
            # Nu er pos en kandidat til pair[0]
#            if pos not in restored_keys.values():
            if pair[0] not in restored_key_candidates:
                restored_key_candidates[pair[0]] = [pos]
#                restored_keys[pair[0]] = pos
            else:
                restored_key_candidates[pair[0]].append(pos)

    # Nu har vi alle kandidaterne, skal fikses op
    visited = []
    candidate_list = [(name, candidates) for (name, candidates) in restored_key_candidates.items()]
    candidate_list.sort(key=lambda x: len(x[1]))
#    print(10*"=")
#    print(candidate_list)
    restored_keys = {}
    for name, candidates in candidate_list:
        good_pos = [pos for pos in candidates if pos not in visited][0]
        visited.append(good_pos)
        restored_keys[name] = good_pos
    return restored_keys

restored_keys = restore_keys(keys, valid_tickets)
print(restored_keys)
my_labeled_ticket = {
        name : myticket[key] for (name, key) in restored_keys.items()
        }
print(my_labeled_ticket)
out_vals = [
    value for (name, value) in my_labeled_ticket.items() if name[:9]=="departure"
    ]
output = 1
for val in out_vals:
    output = output * val
print(output)
