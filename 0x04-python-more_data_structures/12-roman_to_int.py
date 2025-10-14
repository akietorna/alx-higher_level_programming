#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    i = 0
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    while i < len(roman_string):
        if roman_string[i] == "M":
            num += 1000
            i += 1
        elif roman_string[i] == "D":
            num += 500
            i += 1
        elif roman_string[i] == "C":
            if i < len(roman_string) - 1 and roman_string[i + 1] == "M":
                num += 900
                i += 2
            elif i < len(roman_string) - 1 and roman_string[i + 1] == "D":
                num += 400
                i += 2
            else:
                num += 100
                i += 1
        elif roman_string[i] == "L":
            num += 50
            i += 1
        elif roman_string[i] == "X":
            if i < len(roman_string) - 1 and roman_string[i + 1] == "C":
                num += 90
                i += 2
            elif i < len(roman_string) - 1 and roman_string[i + 1] == "L":
                num += 40
                i += 2
            else:
                num += 10
                i += 1
        elif roman_string[i] == "V":
            num += 5
            i += 1
        elif roman_string[i] == "I":
            if i < len(roman_string) - 1 and roman_string[i + 1] == "X":
                num += 9
                i += 2
            elif i < len(roman_string) - 1 and roman_string[i + 1] == "V":
                num += 4
                i += 2
            else:
                num += 1
                i += 1
    return num
