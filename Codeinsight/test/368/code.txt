def test(str0):
    return list(filter(None, map(str.strip, str0.split(','))))