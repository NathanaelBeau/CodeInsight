import re

def test(var0):
    pattern = r"(\d+(\.\d+)?)([KMB]?)"
    match = re.match(pattern, var0.upper())
    if not match:
        return None
    number, _, suffix = match.groups()
    map_dict = {'K': 10**3, 'M': 10**6, 'B': 10**9}
    return float(number) * map_dict.get(suffix, 1)

