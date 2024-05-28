#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    elif length >= 3:
        fibs = [0, 1]
        for i in range(2, length):
            fibs.append(fibs[i-1] + fibs[i-2])
        print(fibs)