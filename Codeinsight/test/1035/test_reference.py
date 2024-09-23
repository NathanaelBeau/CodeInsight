def test(lst0):
    return sorted(range(len(lst0)), key=lambda i: lst0[i], reverse=True)[:2]

