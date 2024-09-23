def test(lst0, var0, attr_name):
    return [item for item in lst0 if getattr(item, attr_name) == var0]
