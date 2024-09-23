def test(lst0):
    return [item for item in lst0 if any(isinstance(x, str) and 'ar' in x for x in item)]
