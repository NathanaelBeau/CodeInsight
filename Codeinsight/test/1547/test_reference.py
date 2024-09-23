def test(var0):
    for char in set(var0):
        if var0.count(char) >= 3:
            var0 = var0.replace(char, '')
    return var0

