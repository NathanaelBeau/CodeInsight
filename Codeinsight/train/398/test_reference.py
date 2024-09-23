def test(s: str, sub: str) -> int:
    count = start = 0
    while start < len(s):
        pos = s.find(sub, start)
        if pos == -1:
            break
        start = pos + 1
        count += 1
    return count
