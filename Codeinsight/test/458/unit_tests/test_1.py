var0, var1, var2 = 0.0, 2.0, 5
result = test(var0, var1, var2)
assert all(var0 <= val <= var1 for val in result), 'Test failed'