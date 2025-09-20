#!/usr/bin/python3
def uppercase(str):
    for a in str:
        print('{}'.format(chr(ord(a) - 32) if ('a' <= a <= 'z') else a), end='')
    print('\n')
