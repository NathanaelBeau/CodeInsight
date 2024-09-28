def test(dict0, var0):
    lowercase_dict = {k.lower(): v for k, v in dict0.items()}
    lowercase_key = var0.lower()
    return lowercase_dict.get(lowercase_key)