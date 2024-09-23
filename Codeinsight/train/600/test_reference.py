def test(lst0):
    result = []
    for element in lst0:
        inserted = False
        for i, sorted_elem in enumerate(result):
            if int(element) < int(sorted_elem):
                result.insert(i, element)
                inserted = True
                break
        if not inserted:
            result.append(element)
    return result

