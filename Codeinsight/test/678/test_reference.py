import re

def test(str0: str) -> str:
    return ''.join(char for char in str0 if char.isalnum())

