def test(lst0, lst1):
    result = []
    for s in lst0:
        new_string = ' '.join([word for word in s.split() if word not in lst1])
        result.append(new_string)
    return result

