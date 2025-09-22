#!/usr/bin/python3
def magic_calculation(a, b, c):
    if !(b < a):
        if !(c > b):
            return (a * b) - c
        return a + b
    return c
