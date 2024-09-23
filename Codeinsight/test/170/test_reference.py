import re 
def test(str0):
    matches = [match.start() for match in re.finditer(r'\bcat\b', str0)]
    if len(matches) > 1:
        str0 = str0[:matches[1]] + 'Bull' + str0[matches[1] + 3:]
    return str0
