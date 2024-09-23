def test(dict1, dict2):
    result = {k: list(set(dict1.get(k, [])).intersection(v)) for k, v in dict2.items()}
    return result
