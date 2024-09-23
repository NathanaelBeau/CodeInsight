def test(lst0):
    max_value = max(lst0)
    return [index for index, value in enumerate(lst0) if value == max_value]
