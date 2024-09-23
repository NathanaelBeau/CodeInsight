def test(lst0, var0):
    formatted_result = [list(map(lambda flt: var0.format(flt), sublist)) for sublist in lst0]
    return formatted_result
