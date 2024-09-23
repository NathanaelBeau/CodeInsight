def test(str0, var0):
    parts = str0.split(var0)
    result = var0.join(parts[:-1])  
    return result

