def test(str0):
    temp = str0.split("*")
    return [temp[0] + x for x in temp[1:]]
