def test(dict0, dict1):
    return {k: dct0[k] for k in set(dct0.keys()) & set(dct1.keys())}
