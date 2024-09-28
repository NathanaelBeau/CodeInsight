import re
def test(var0, dict0):
    return re.sub(r'\b\w+\b', lambda m: dict0.get(m.group(0), m.group(0)), var0)
