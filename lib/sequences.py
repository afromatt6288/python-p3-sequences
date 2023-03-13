#!/usr/bin/env python3

def print_fibonacci(length):
    fib_seq = []
    if length > 0:
        fib_seq.append(0)
        if length > 1:
            fib_seq.append(1)
            if length > 2:
                for i in range(2, length):
                    fib_seq.append(fib_seq[i-1]+fib_seq[i-2])
    print(fib_seq)

    pass