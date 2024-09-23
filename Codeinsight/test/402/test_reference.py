def test(var0):
    return [name for name, value in locals().items() if value is var0][0]

