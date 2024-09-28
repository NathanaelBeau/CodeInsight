def test(var0):
    return next(name for name, value in locals().items() if value is var0)
