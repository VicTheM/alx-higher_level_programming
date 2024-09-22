#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    num = 0
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    for i, c in enumerate(roman_string):
        if roman[c]:
            num += roman[c]
            if roman[c] > roman[roman_string[i - 1]] and i > 0:
                num -= 2 * roman[roman_string[i - 1]]
        else:
            return 0
    return num
