def test(lst0):
    result = []
    for i in lst0:
        concatenated_string = ''
        for item in i:
            concatenated_string += item
        result.append(concatenated_string)
    return result

