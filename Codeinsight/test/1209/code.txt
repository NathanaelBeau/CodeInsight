def test(dict0):
    return {k: v for k, v in sorted(dict0.items(), key=lambda item: max(item[1]), reverse=True)}
