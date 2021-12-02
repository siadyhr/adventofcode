def interpret(program):
    visited = []
    acc = 0
    pos = 0
    exit_code = -1   #0: halt, 1: loop
    while pos not in visited:
        visited.append(pos)
        try:
            instruction = program[pos]
        except IndexError:
            end_condition = "halted"
            break
        if instruction[0] == "jmp":
            pos = pos + instruction[1]
            continue
        elif instruction[0] == "acc":
            acc = acc + instruction[1]
        elif instruction[0] == "nop":
            pass
        pos += 1

    return {
        "visited"   : visited,
        "acc"       : acc,
        "pos"       : pos,
        "exit_code" : exit_code,
    }
