#  https://leetcode.com/problems/roman-to-integer/
from enum import Enum


class RomanNumeral(Enum):
    I = 1
    IV = 4
    V = 5
    IX = 9
    X = 10
    XL = 40
    L = 50
    XC = 90
    C = 100
    CD = 400
    D = 500
    CM = 900
    M = 1000


def converter(string):
    previousNumber = 0
    result = 0
    RomanNumeral = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400,
                    'D': 500, 'CM': 900, 'M': 1000}

    for i in reversed(string):
        current_value = RomanNumeral[i]

        if current_value >= previousNumber:
            result += current_value

        elif current_value < previousNumber:
            result -= current_value

        previousNumber = current_value

    return result


if __name__ == '__main__':
    roman = 'MXLVC'
    print(converter(roman))
