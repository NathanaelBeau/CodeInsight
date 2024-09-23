def test(lst0, var0):
    closest_number = min(lst0, key=lambda x: abs(x - var0))
    return closest_number

