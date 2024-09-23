def test(var0, lst0):
    return ' '.join([word for word in var0.split() if word.lower() not in set(lst0)])

