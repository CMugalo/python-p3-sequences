#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = []
    if length == 0:
        print(fib_list)
    elif length == 1:
        fib_list.append(0)
        print(fib_list)
    elif length > 1:
        fib_list.append(0)
        i = 2
        while i <= length:
            fib_list.append(i - 1)
            updated_list = fib_list
            
            #fib_list.append((fib_list[i] + fib_list[i-1]))
            print(fib_list)
            i += 1