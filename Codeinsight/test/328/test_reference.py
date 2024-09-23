def test(dict0, lst0):
    return {k: dict0.get(k) for k in lst0 if k in dict0}