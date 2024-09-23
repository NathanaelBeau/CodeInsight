import re
def test(str0):
    matches = []
    start = 0
    
    while start < len(str0):
        match = re.match(r'(\d+)([A-Z])', str0[start:])
        if match:
            num, char = match.groups()
            matches.append((num, char))
            start += len(num) + len(char)
        else:
            start += 1
    
    return matches

