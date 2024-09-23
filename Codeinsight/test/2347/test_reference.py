def test(str0, str1):
    default_sep = str1[0]
    for sep in str1[1:]:
        str0 = str0.replace(sep, default_sep)
    return [i.strip() for i in str0.split(default_sep)]

