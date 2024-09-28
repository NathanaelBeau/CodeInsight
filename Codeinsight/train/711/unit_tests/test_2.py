df0 = pd.DataFrame({'data': ['1,2,3', '4,5'], 'other': ['6,7', '8,9']})
var0 = 'data'
expected_result =  pd.Series(['1', '2', '3', '4', '5'])
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'