import sys
import functools

@functools.lru_cache
def countConfigs(xs, instructions):
    if len(xs) < sum(instructions) + len(instructions) - 1:
        return 0
    elif xs == "":
        if instructions == ():
            return 1
        return 0
    elif instructions == ():
        if "#" in xs:
            return 0
        return 1
    elif len(instructions) == 1:
        if (
                (instructions[0] == len(xs))
                and
                all(map(lambda x: x in "#?", xs))
        ):
            return 1
#        if (
#                all(map(lambda x: x in "#?", xs[:instructions[0]]))
#                and
#                all(map(lambda x: x in "#?", xs[:instructions[0]]))
#            ):
#            return 1
#        return 0
    if xs[0] == '.':
        return countConfigs(xs[1:], instructions)
    elif xs[0] == '#':
        if (
                all(map(lambda x: x in "?#", xs[:instructions[0]]))
            ) and (
                    xs[instructions[0]] in ".?"
                    ):
                return countConfigs(xs[instructions[0]+1:], instructions[1:])
        return 0
    elif xs[0] == "?":
        return (
                countConfigs(xs[1:], instructions)
                +
                countConfigs("#" + xs[1:], instructions)
                )
result1 = 0
result2 = 0

for i, rawIn in enumerate(sys.stdin):
    splittedInput = rawIn.split(" ")
    xs = splittedInput[0]
    instructions = [int(x) for x in splittedInput[1].split(",")]
    result1 += countConfigs(xs, tuple(instructions))
    result2 += countConfigs((5*("?"+xs))[1:], tuple(5*instructions))

print("Part 1:", result1)
print("Part 2:", result2)
