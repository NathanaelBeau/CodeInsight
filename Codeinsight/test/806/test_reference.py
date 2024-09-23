import re

def test(dict0, var0):
    regex = re.compile(r'\b(' + '|'.join(map(re.escape, dict0.keys())) + r')\b', flags=re.IGNORECASE)
    return regex.sub(lambda match: dict0[match.group(0).lower()], var0)

