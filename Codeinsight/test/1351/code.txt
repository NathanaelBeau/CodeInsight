import re

def test(str0, dict0):
    regex = re.compile("(%s)" % "|".join(map(re.escape, dict0.keys())))
    return regex.sub(lambda mo: dict0[mo.string[mo.start():mo.end()]], str0)
