ser0 = pd.Series([1, 2, 3])
var0 = 0
result = test(ser0, var0)
expected = pd.Series([1, 2, 3])
assert result.equals(expected), 'Test failed'