ser0 = pd.Series([1, 2, 3])
var0 = -2
result = test(ser0, var0)
expected = pd.Series([-1, 0, 1])
assert result.equals(expected), 'Test failed'