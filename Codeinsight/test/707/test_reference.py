import random

def test(dict0):
    total = sum(dict0.values())
    pick = random.uniform(0, total)
    current = 0
    for key, value in dict0.items():
        current += value
        if current > pick:
            return key
