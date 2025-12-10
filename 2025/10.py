#06.50
import sys
import functools
data = [
        line[:-1].split(" ")
        for line in sys.stdin
        ]

goals = [
        [1 if x=="#" else 0 for x in line[0][1:-1]]
        for line in data]
buttons = [
        [
            tuple(map(int, x[1:-1].split(",")))
            for x in line[1:-1]
        ]
        for line in data
        ]

new_buttons = [
        [
            [1 if i in button else 0 for i in range(len(goal))]
            for button in button_list
        ]
        for button_list, goal in zip(buttons, goals)
    ]
joltages = [
        tuple(map(int, line[-1][1:-1].split(",")))
        for line in data
        ]

#print(data[0])
#print(goals)
#print(buttons)
#print(new_buttons)
#print(joltages)

def min_presses(result, buttons):
#    print("Minpresses")
#    print(buttons)
#    print(result)
    def combination_works(result, buttons, combination):
        # sum combination[i] * button[i]
        # hver indgang:
        #   sum_i: button[i][j] * combination[i]
#        print("Check", combination)
        a = [
                [c * x for x in button]
                for c, button in zip(combination, buttons)
            ]
        a = [sum(x)%2 for x in zip(*a)]
#        print("got", a)
        return a == result
    combinations = [
            [int(x) for x in bin(i)[2:].rjust(len(buttons), "0")]
            for i in range(2**len(buttons))
    ]
#    print("Hej")
    combinations.sort(key = lambda x : sum(x))
    for combination in combinations:
        if combination_works(result, buttons, combination):
#            print("Succes!")
#            print(combination)
#            print("%s presses" % sum(combination))
            return sum(combination)

result = 0
for goal, button in zip(goals, new_buttons):
    result += min_presses(goal, button)
print("Part 1:", result) #07.35
