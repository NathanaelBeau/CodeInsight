var0 = 20
var1 = 7
result = test(var0, var1)
assert len(result) == len(set(result)) and all([num < var0 for num in result]), 'Test failed'