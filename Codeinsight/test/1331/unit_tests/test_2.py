df0 = pd.DataFrame({'x': [13, 14], 'y': [14, 13]})
df1 = pd.DataFrame({'x': [15, 16], 'y': [12, 11]})
var0 = 'y'
expected_result =  pd.DataFrame({'x': [16, 15, 14, 13], 'y': [11, 12, 13, 14]})
result = test(df0, df1, var0)
assert result.equals(expected_result), 'Test failed'