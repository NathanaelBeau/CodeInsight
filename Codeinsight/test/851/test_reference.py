import re

def test(str0: str) -> bool:
    return bool(re.match(r'^[a-zA-Z0-9_-]*$', str0))

