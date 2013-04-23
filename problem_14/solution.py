#!/usr/bin/env python


def collatz_generator(start):
    yield start
    while start > 1:
        if start % 2 == 0:
            yield start / 2
            start = start / 2
        else:
            yield (3 * start) + 1
            start = (3 * start) + 1

if __name__ == "__main__":
    assert [13, 40, 20, 10, 5, 16, 8, 4, 2, 1] == list(collatz_generator(13))
    longest_sequence = 0
    candidate = 0
    for start in range(10 ** 6):
        sequence_length = len(list(collatz_generator(start)))
        if sequence_length > longest_sequence:
            longest_sequence = sequence_length
            candidate = start
    print(candidate)