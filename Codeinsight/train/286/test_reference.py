import re

def test(s: str) -> str:
    return re.sub(r'[\W_]+', '', s, flags=re.UNICODE)

