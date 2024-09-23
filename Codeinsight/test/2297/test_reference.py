def test(lst0):
    if not lst0:
        return []
    else:
        return [sum(lst0[:i+1]) for i in range(len(lst0))]