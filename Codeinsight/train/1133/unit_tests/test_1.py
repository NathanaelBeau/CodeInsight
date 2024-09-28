df0 = pd.DataFrame({'X': ['apple'], 'Y': ['banana'], 'Z': ['cherry']})
var0 = 2
expected_result =  pd.Series(['cherry'], name='Z')
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'