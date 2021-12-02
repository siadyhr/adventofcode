import sys
import re

# http://adventofcode.com/2020/day/8

program = []
for rawin in sys.stdin:
    rawin = rawin[:-1] # newlinestrip
#    print('"' + rawin + '"')
    rawin = rawin.split()
    if rawin:
#        print(rawin)
        program.append((rawin[0], int(rawin[1])))
    else:
        pass

#print(program)

def interpret(program):
    visited = []
    acc = 0
    pos = 0
    halted = False
    while pos not in visited:
        visited.append(pos)
        try:
            instruction = program[pos]
        except IndexError:
            halted = True
            break
#        print(pos)
        if instruction[0] == "jmp":
            pos = pos + instruction[1]
            continue
        elif instruction[0] == "acc":
            acc = acc + instruction[1]
        elif instruction[0] == "nop":
            pass
        pos += 1
    return visited, acc, pos, halted

for i in range(len(program)):
    newprog = program.copy()
    if newprog[i][0] == "jmp":
        newprog[i] = ("nop", newprog[i][1])
    elif newprog[i][0] == "nop":
        newprog[i] = ("jmp", newprog[i][1])
    else:
#        print(i)
        continue
    _, acc, _, halted = interpret(newprog)
    if halted:
        print(acc)
        quit()

#print(interpret(program)[1])
