import re
def test(str0):
    pattern = r'(\d+)([A-Z])'
    matches = re.findall(pattern, str0)
    return [(match[0], match[1]) for match in matches]
