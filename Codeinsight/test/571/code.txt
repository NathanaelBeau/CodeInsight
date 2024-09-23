import re

def test(str0: str) -> float:
    matches = re.findall(r'[-+]?\d*\.\d+|\d+', str0)
    return float(matches[0]) if matches else None
