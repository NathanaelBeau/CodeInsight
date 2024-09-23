import difflib

def test(var0, var1):
    diff = list(difflib.ndiff(var0, var1))
    insertions = [item[2:] for item in diff if item.startswith('+ ')]
    return ''.join(insertions)

