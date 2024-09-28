
def test(lst0):
    return [a + b for i, a in enumerate(lst0) for j, b in enumerate(lst0) if i != j]
