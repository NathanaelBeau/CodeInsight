def test(lst0):
    return sorted(lst0, key=lambda s: [int(i) for i in s.split('.')])
