def test(var0, var1):
    start = 0
    indices = []
    while True:
        start = var1.find(var0, start)
        if start == -1:
            return indices
        indices.append(start)
        start += len(var0)