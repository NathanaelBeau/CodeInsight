df0 = pd.DataFrame({ 'month': ['Jan', 'Feb', 'Mar'], 'value': [10, 20, 30] })
var0 = 'month'
expected_result =  pd.DataFrame({ 'value': [10, 20, 30] }, index=['Jan', 'Feb', 'Mar'])
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'