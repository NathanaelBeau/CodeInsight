def test(var0):
    while '**' in var0:
        var0 = var0.replace('**', '*')
    return var0
