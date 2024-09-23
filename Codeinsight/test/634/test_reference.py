import re

def test(dict0, var0):
    regex = re.compile("(%s)" % "|".join(map(re.escape, dict0.keys())), re.IGNORECASE)
    return regex.sub(lambda match: dict0[match.group(0).lower()], var0)


