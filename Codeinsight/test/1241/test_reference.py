def test(var0):
    for k, v in list(locals().items()):
        if v is var0:
            variable_name_as_str = k
    return variable_name_as_str
