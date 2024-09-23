import re

def test(str0: str) -> list:
    return [item for item in re.split(r'(?=[A-Z])', str0) if item]
