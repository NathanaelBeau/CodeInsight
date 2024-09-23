def test(var0, replacements):
    for old, new in replacements.items():
        var0 = var0.replace(old, new)
    return var0

