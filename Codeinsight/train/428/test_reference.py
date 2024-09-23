def test(str0: str, substring: str) -> list:
    indices = []
    idx = str0.find(substring)
    while idx != -1:
        indices.append(idx)
        idx = str0.find(substring, idx + 1)
    return indices
