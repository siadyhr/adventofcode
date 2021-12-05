import sys

def input_to_segment(raw):
    splits = raw.split()
    return tuple(
            tuple(
                int(x) for x in splits[i].split(',')
                )
            for i in (0, 2)
            )

def count_n_overlaps(segments, n, straight=True):
    n_overlaps = 0
    board = {}
    for (x0, y0), (x1, y1) in segments:
        if (x0 == x1 or y0 == y1):
            for x in range(min(x0, x1), max(x0, x1) + 1):
                for y in range(min(y0, y1), max(y0, y1) + 1):
                    try:
                        board[(x, y)] += 1
                        if board[(x, y)] == n:
                            n_overlaps += 1
                    except KeyError:
                        board[(x, y)] = 1
        elif not straight:
            if x0 < x1:
                y_start = y0
            else:
                y_start = y1
            for i, x in enumerate(range(min(x0, x1), max(x0, x1) + 1)):
                if (y1 - y0)/(x1 - x0) > 0:
                    dy = 1
                else:
                    dy = -1

                try:
                    board[(x, y_start + dy*i)] += 1
                    if board[(x, y_start + dy*i)] == n:
                        n_overlaps += 1
                except KeyError:
                    board[(x, y_start + dy*i)] = 1

    return n_overlaps


segments = [input_to_segment(line) for line in sys.stdin]
# Part 1
print(count_n_overlaps(segments, 2))
# Part 2
print(count_n_overlaps(segments, 2, straight=False))
