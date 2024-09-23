import re

def test(lst0: list):
    results = []
    for item in lst0:
        results.append(re.sub(r" \(\w+\)", "", item))
    return results

