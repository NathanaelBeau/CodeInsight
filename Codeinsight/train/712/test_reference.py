import random

def test(lst0):
    index = random.randrange(len(lst0))
    lst0[index] = "modified_value"
    return lst0

