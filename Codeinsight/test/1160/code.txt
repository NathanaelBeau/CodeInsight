def test(var0, var1, var2=1):
    words = var0.split()
    if var1 in words:
        idx = words.index(var1)
        return tuple(words[max(idx - var2, 0):idx] + words[idx + 1: idx + 1 + var2])
