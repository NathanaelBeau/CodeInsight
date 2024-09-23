def test(lst0, lst1):
    return [result - subtractor for result, subtractor in zip(lst0, lst1)]