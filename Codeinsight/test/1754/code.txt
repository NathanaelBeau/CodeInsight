import random

def test(var0):
    return ''.join([char.upper() if random.choice([True, False]) else char.lower() for char in var0])
