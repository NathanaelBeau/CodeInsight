import re
def test(pattern0, var0):
    return [match.group(1) for match in re.finditer(r"(?=(" + pattern0 + "))", var0)]
