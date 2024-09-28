def test(lst0):
    return [sum(int(char) for char in s if char.isdigit()) for s in lst0]
