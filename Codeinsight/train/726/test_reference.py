def test(str0, tpl0):
    clean_str = str0.strip("()").split(",")
    tuple_from_str = tuple(map(type(tpl0[0]), clean_str))
    return tpl0 + tuple_from_str
