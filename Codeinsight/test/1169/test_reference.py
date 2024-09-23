def test(lst0):
    from collections import defaultdict
    result = defaultdict(int)
    for d in lst0:
        for key, value in d.items():
            result[key] += value
    return dict(result)

