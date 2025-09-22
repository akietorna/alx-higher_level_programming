#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    for a in range(len(str)):
        if a != n:
            newstr += str[a]
    return (newstr)
