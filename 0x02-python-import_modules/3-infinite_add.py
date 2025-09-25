#!/usr/bin/python3
from sys import argv

res = 0

if __name__ == '__main__':
    for a in range(1, len(argv)):
        res += int(argv[a])
    print(res)
