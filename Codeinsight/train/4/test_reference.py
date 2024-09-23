def test(dict0, index0):
    return {k: v for k, v in sorted(dict0.items(), key=lambda item: item[1][index0])}

