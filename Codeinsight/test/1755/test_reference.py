def test(arr0, val0):
    coordinates = [(i, row.index(val0)) for i, row in enumerate(arr0) if val0 in row]
    return coordinates[0] if coordinates else None

