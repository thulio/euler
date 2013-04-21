#!/usr/bin/env python
from problem_2.solution_2 import fibonnaci

FIBO_NUMBERS = [(index, number) for index, number in enumerate(fibonnaci(9999))]


if __name__ == "__main__":
    numbers = list(filter(lambda x: len(str(x[1])) == 1000, FIBO_NUMBERS))
    print(numbers[0])