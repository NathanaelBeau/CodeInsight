import re

def test(str0, var0):
    sentences = re.match(r'(.*?[.?!](?:\s+.*?[.?!]){0,' + str(var0 - 1) + '})', str0)
    if sentences:
        return sentences.group(1)
    else:
        return str0
