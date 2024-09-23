import re

def test(var0):
    match = re.search(r'(?<=v=)[^&#]+', var0) or re.search(r'(?<=be/)[^&#]+', var0)
    return match.group() if match else None

