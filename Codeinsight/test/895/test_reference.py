def test(str0, str1):
    return "".join([s + str0 for s in str1])[:-len(str0)]
