df0 = pd.DataFrame({'E': ['P', 'P', 'P'], 'F': [7, 8, 9]})
var0 = 'E'
var1 = 'F'
expected_result =  pd.Series(data=[24], index=['P'])
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'