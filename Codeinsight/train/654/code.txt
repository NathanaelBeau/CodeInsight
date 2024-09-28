def test(lst0, dict0):
    return [sorted(item, key=dict0.get) for item in lst0]
