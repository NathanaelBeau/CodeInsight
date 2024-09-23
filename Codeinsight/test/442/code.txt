import random

def random_case(char):
    return char.upper() if random.choice([True, False]) else char.lower()

def test(var0):
    return ''.join(map(random_case, var0))
