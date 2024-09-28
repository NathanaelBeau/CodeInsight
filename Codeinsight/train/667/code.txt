def test(dict0):
    return [*map(dict, zip(*[[(k, v) for v in value] for k, value in dict0.items()]))]