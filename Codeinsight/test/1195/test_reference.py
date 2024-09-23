import re

def test(var0):
    numbers = []
    num = ""
    for char in var0:
        if char.isdigit():
            num += char
        elif num:
            numbers.append(num)
            num = ""
    if num:
        numbers.append(num)
    return numbers
