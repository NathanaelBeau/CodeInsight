var0 = "Python"
result = test(var0)
assert len(result) == len(var0) and all(c1.lower() == c2.lower() for c1, c2 in zip(result, var0)), 'Test failed'