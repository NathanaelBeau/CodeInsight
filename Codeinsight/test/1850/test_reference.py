def test(lst0, lst1):
    result = []
    for item in lst0:
        for x in lst1:
            if x in item:
                result.append(item)
                break
    return result
