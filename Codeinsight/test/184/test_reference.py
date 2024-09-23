import re
def test(var0):
    numbers = re.findall(r'\d+', var0)
    chars = re.findall(r'[A-Za-z]+', var0)
    return numbers, chars
