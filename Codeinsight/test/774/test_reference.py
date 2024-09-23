def test(str0):
    parts = str0.split("*")
    expanded = [parts[0] + x for x in parts[1:]]
    return expanded
