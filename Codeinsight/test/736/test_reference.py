from functools import reduce

def extract_element(lst, index):
    return lst[index]

def test(lst0, lst1):
    return list(map(lambda i: extract_element(lst0, i), lst1))