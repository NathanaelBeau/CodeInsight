import re
def test(var0, var1, var2=1):
    pattern = r'(?:(\w+)\W+)?' * var2 + r'\b{}\b'.format(re.escape(var1)) + r'(?:\W+(\w+))?' * var2
    match = re.search(pattern, var0)
    if match:
        return match.groups()
