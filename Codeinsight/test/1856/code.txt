def test(var0, var1, lst0):
    returned_tuples = []
    for item in lst0:
        if item[var0] == var1:
            returned_tuples.append(item)
    return returned_tuples
