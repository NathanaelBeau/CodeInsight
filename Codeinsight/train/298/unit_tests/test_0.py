var0, var1, var2, var3 = 0, 50, 10, 4
result = test(var0, var1, var2, var3)
assert result.shape == (var2, var3) and (result.values >= var0).all() and (result.values < var1).all(), 'Test failed'