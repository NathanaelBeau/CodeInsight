import re

def test(str0):
    return [i[0] for i in re.findall(r'((\d)(?:[()]*\2*[()]*)*)', str0)]
