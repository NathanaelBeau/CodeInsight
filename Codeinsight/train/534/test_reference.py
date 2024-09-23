def test(str0, lst0):
    default_sep = lst0[0]
    for sep in lst0[1:]:
        str0 = str0.replace(sep, default_sep)
    return [i.strip() for i in str0.split(default_sep)]
