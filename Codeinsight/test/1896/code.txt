import re

def test(var0, char_start, char_end):
    pattern = r'(?<=[{0}])([^{1}]+)(?=[{1}])'.format(re.escape(char_start), re.escape(char_end))
    return re.findall(pattern, var0)