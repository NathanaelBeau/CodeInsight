import re

def test(var0):
    numbers = []
    number = ''
    for char in var0:
        if char.isdigit():
            number += char
        elif number:
            numbers.append(number)
            number = ''
    if number:
        numbers.append(number)
    return numbers

