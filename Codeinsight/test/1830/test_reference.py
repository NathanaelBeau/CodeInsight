import re

def test(str0:str, regex_str:str) -> tuple:
    regex = re.compile(regex_str, re.I + re.S)
    matches = regex.findall(str0)
    return tuple(matches)
