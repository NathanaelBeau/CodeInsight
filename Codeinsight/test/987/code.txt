def test(lst0, dict0):
    result = []
    for item in lst0:
        sorted_item = sorted(item, key=dict0.get)
        result.append(sorted_item)
    return result

