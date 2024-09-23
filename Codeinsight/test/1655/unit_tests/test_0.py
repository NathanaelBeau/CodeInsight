df0 = pd.DataFrame({'A': ['X', 'Y', 'X', 'Z'], 'B': [1, 2, 3, 4]})
var0 = 'A'
var1 = 'B'
expected_result =  pd.Series(data=[4, 2, 4], index=['X', 'Y', 'Z'])
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'