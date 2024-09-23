import re

def test(str0: str) -> bool:
    return all(char.isalnum() or char in ['_', '-'] for char in str0)
