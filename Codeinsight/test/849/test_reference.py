def test(lst0):
    first_occurrences = {}
    result = []
    
    for item in lst0:
        if item[0] not in first_occurrences:
            first_occurrences[item[0]] = True
            result.append(item)
    
    return result

