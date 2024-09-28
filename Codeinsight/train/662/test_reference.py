def test(str0: str, pattern: str) -> list:
    matches = []
    i = str0.find(pattern)
    while i != -1:
        matches.append(i)
        i = str0.find(pattern, i+1)
    return matches