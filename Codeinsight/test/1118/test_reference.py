import re

def test(str0):
    numbers = ''.join(sorted([char for char in str0 if char.isdigit()]))
    letters = ''.join(sorted([char for char in str0 if char.isalpha()]))
    return numbers + letters
