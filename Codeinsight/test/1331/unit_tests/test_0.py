df0 = pd.DataFrame({'x': [1, 2], 'y': [3, 4]})
df1 = pd.DataFrame({'x': [5, 6], 'y': [1, 2]})
var0 = 'y'
expected_result =  pd.DataFrame({'x': [5, 6, 1, 2], 'y': [1, 2, 3, 4]})
result = test(df0, df1, var0)
assert result.equals(expected_result), 'Test failed'