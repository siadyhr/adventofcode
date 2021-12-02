import sys
import re
import functools
import copy

# http://adventofcode.com/2020/day/14

instructions = []
memory = {}
for rawin in sys.stdin:
    rawin = rawin[:-1] # newlinestrip
#    print('"' + rawin + '"')
    if rawin:
        rawin = [x.strip() for x in rawin.split("=")]
        if rawin[0][:3] == "mem":
            instructions.append(["mem", int(rawin[0][4:-1]), bin(int(rawin[1]))[2:].rjust(36, "0")])
        elif rawin[0][:4] == "mask":
            instructions.append(rawin)
        else:
            print(rawin)
            print("!!!")
#        print(rawin)
    else:
        pass
def bitmask(mask, bits):
    out = "".join([
        bit if m=="X" else m for bit,m in zip(bits, mask)
        ])
    return out

def bitmask2(mask, bits):
    out = "".join([
        bit if m == "0" else m for bit,m in zip(bits, mask)
        ])
    return out

def perms(mask):
    if len(mask) == 1:
        if mask == "X":
            return ["0", "1"]
        return mask
    out = perms(mask[1:])
    if mask[0] == "X":
        return ["0" + perm for perm in out] + ["1" + perm for perm in out]
    return [mask[0] + perm for perm in out]

print(instructions[:10])
current_mask = ""
part1 = False
if part1:
    for instruction in instructions:
        if instruction[0] == "mask":
            current_mask = instruction[1]
        else:
    #        print(instruction[2])
    #        print(current_mask)
            memory[instruction[1]] = bitmask(current_mask, instruction[2])

    print(memory)
else:
    for instruction in instructions:
        if instruction[0] == "mask":
            current_mask = instruction[1]
        else:
            addr = bin(instruction[1])[2:].rjust(36, "0")
            masked_addr = bitmask2(current_mask, addr)
            for perm in perms(masked_addr):
                memory[int(perm, 2)] = instruction[2]

print(sum(
    int(value, 2) for value in memory.values()
    ))
