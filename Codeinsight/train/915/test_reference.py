

def test(lst0):
    result = []
    for tup in lst0:
        for item in tup:
            result.append(item)
    return result