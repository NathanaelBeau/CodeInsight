def test(dict0):
    return {k: 'updated' for k, v in dict0.items() if v is None}
