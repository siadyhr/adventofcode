import sys
import re
import functools
import copy

# http://adventofcode.com/2020/day/18

part = 2
data = []
raw_data = []
for rawin in sys.stdin:
    rawin = rawin[:-1] # newlinestrip
#    print('"' + rawin + '"')
    if rawin:
        data.append(rawin.split())
        raw_data.append(rawin)
#        print(rawin)
    else:
        pass

def eval_simple(expression):
    # Evaluer uden ( )
    result = int(expression[0])
    operation = "+"
    for char in expression[1:]:
        try:
            if operation == "+":
                result += int(char)
            else:
                result *= int(char)
        except ValueError:
            operation = char
    return result

def eval_simple_flipped(expression):
    # Evaluer uden ( ), + før *
    print("esf", expression)
    if len(expression) == 1:
        return expression[0]
    try:
        first_plus = min([i for i, char in enumerate(expression) if char == "+"]) 
        print("i+:", first_plus)
    except ValueError:
        print("ValErr")
        print(expression)
        return str(eval_simple(expression))

    return eval_simple_flipped(
        expression[:first_plus-1]
        +
        [str(int(expression[first_plus-1]) + int(expression[first_plus+1]))]
        +
        expression[first_plus+2:]
    )

def get_inner(expression):
    starts = []
    ends = []
    for char in expression:
        starts.append(char.count("("))
        ends.append(char.count(")"))
    if sum(ends) == 0:
        return

    first_end = min([i for i, val in enumerate(ends) if val > 0])
    matching_start = max([i for i, val in enumerate(starts) if val > 0 and i <= first_end ])

    return {
        "start"   : matching_start,
        "end"     : first_end,
        "n_start" : starts[matching_start],
        "n_end"   : ends[first_end],
    }


def eval_expr(expression):
    while True:
        inner_location = get_inner(expression)
        print(inner_location)
        if inner_location is None:
            break
        inner_expr = expression[inner_location["start"]:inner_location["end"]+1]
        inner_expr_stripped = [
            "".join([char for char in inner_expr[0] if char != "("])
            ,
            *[char for char in inner_expr[1:-1]]
            ,
            "".join([char for char in inner_expr[-1] if char != ")"])
            ]
        print("Indre:", inner_expr_stripped)
        if part == 1:
            inner_result = eval_simple(inner_expr_stripped)
        else:
            inner_result = eval_simple_flipped(inner_expr_stripped)
        print("Giver:", inner_result)
        insert = (
                "(" * (inner_location["n_start"] - 1)
                +
                str(inner_result)
                +
                ")" * (inner_location["n_end"] - 1)
        )
        print("i", insert)
        expression[inner_location["start"]:inner_location["end"]+1] = [insert]
        print("Indsat.", expression)

    print("Done!", expression)
    return eval_simple(expression) if part == 1 else eval_simple_flipped(expression)

partials = []
def get_total(data):
    total = 0
    for line in data:
        print(line)
        partial_result = int(eval_expr(line))
        print("part")
        print(partial_result)
        partials.append(partials)
        print(partial_result)
        total += partial_result
    return total

print(get_total(data))
#print(partials)
