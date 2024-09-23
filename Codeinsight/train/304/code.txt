import re

def test(var0):
    return re.sub('[^a-zA-Z0-9-_*.]', '', var0)
