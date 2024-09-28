import re
def test(str0: str, pattern: str) -> list:
    matches = re.findall(pattern, str0)
    indices = [m.span() for m in re.finditer(pattern, str0)]
    return [(start, end, value) for (start, end), value in zip(indices, matches)]
