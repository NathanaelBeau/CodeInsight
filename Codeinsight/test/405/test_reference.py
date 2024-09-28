def test(lst0):
    formatted_result = [['{0:.8e}'.format(flt) for flt in sublist] for sublist in lst0]
    return formatted_result
