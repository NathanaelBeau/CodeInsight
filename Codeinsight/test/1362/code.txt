def test(str0, str1):
    matching = []
    for i in str0:
        if i.__contains__(str1):
            matching.append(i)
    return matching
