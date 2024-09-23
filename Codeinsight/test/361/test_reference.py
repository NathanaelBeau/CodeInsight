import re

def test(str0, var0):
    return re.match(rf'(.*?[.?!](?:\s+.*?[.?!]){{0,{var0 - 1}}})', str0).group(1)

