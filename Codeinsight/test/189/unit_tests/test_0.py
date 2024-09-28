ser0 = pd.Series([1, 2, 3])
var0 = 5
result = test(ser0, var0)
expected = pd.Series([6, 7, 8])
assert result.equals(expected), 'Test failed'