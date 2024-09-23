import re

def test(var0, regex_pattern):
    matches = [m.start() for m in re.finditer(r"(?!{})\w".format(regex_pattern), var0)]
    return matches[-1] if matches else None

