df0 = pd.DataFrame({'C': ['M', 'M', 'N'], 'D': [5, 5, 6]})
var0 = 'C'
var1 = 'D'
expected_result =  pd.Series(data=[10, 6], index=['M', 'N'])
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'