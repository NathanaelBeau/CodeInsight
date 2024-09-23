import re
import string

def test(var0):
    return re.sub(r'[{}]'.format(string.punctuation), '', var0)

