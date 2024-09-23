def test(lst0, var0):
    formatted_result = [[var0.format(flt) for flt in sublist] for sublist in lst0]
    return formatted_result

