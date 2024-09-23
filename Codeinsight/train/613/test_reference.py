import re

def test(str0):
    regexStr = r'^([^@]+)@[^@]+$'
    matchobj = re.search(regexStr, str0)
    if matchobj is not None:
        return matchobj.group(1)
    else:
        return "Did not match"
