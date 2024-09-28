var0, var1, var2 = -5.0, 0.0, 7
result = test(var0, var1, var2)
assert all(var0 <= val <= var1 for val in result), 'Test failed'