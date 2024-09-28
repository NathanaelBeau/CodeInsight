def test(lst0):
    return [max(column, key=len) for column in zip(*lst0)]
