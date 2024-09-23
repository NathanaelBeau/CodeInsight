import random

def test(lst0):
    random_choice = random.choice(lst0)
    index = lst0.index(random_choice)
    lst0[index] = "modified_value"
    return lst0
