import re

def test(str0: str) -> float:
    match = re.search(r'[-+]?\d*\.\d+|\d+', str0)
    return float(match.group()) if match else None
