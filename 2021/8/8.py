import sys

def part1(results):
    return sum(len(result) in (2,4,3,7) for case in results for result in case)
    # 2,4,3,7 is #segments in 1, 4, 7, 8

def decode(attempts):
    '''
    Length 2, 4, 3, 7 gives number (1, 4, 7, 8)
    Length 5: (2, 3, 5):
        Snit: ADG
    Length 6: (0, 6, 9):
        Snit: 'ABFG'
    '''

    decoded = {x : -1 for x in attempts}
    one = [x for x in attempts if len(x) == 2][0]
    four = [x for x in attempts if len(x) == 4][0]

    decoded[one] = 1
    decoded[four] = 4

    for number in attempts:
        if len(number) == 3:
            decoded[number] = 7
        elif len(number) == 7:
            decoded[number] = 8
        elif len(number) == 5:
            if len(set(number) & set(one)) == 2:
                decoded[number] = 3
            elif len(set(number) & set(four)) == 2:
                decoded[number] = 2
            else:
                decoded[number] = 5
        elif len(number) == 6:
            if len(set(number) & set(four)) == 4:
                decoded[number] = 9
            elif len(set(number) & set(one)) == 2:
                decoded[number] = 0
            else:
                decoded[number] = 6

    return decoded

        
def part2(attempts, results):
    output = 0
    for case_attempts, case_results in zip(attempts, results):
        decoded = decode(["".join(sorted(x)) for x in case_attempts])
        output += sum(10**(4-i-1) * decoded["".join(sorted(num))] for i, num in enumerate(case_results))
    return output

attempts = []
results = []
for line in sys.stdin:
    raw = line.split('|')
    attempts.append(raw[0].split())
    results.append(raw[1].split())

# part 1
print(part1(results))
print(part2(attempts, results))
