def test(str0):
    import re
    return re.sub(r'(?<!^)([A-Z])', r' \1', str0)
