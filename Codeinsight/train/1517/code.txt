def test(d: dict) -> list:
    return [{'key1': val1, 'key2': val2} for val1, val2 in zip(d['key1'], d['key2'])]
