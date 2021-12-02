import sys

answers = set()
answers2 = []
N = 0
N2 = 0
for rawin in sys.stdin:
    rawin = rawin[:-1] # newlinestrip
    print('"' + rawin + '"')
    if rawin:
        answers.update(set(rawin))
        answers2.append(set(rawin))
        print(answers2)
    else:
        print()
        N += len(answers)
        N2 += len(answers2[0].intersection(*answers2[1:]))
        answers = set()
        answers2 = []

print(N)
print(N2)
