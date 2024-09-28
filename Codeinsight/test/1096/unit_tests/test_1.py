df0 = pd.DataFrame({ 'month': ['Apr', 'May', 'Jun'], 'value': [40, 50, 60] })
var0 = 'month'
expected_result =  pd.DataFrame({ 'value': [40, 50, 60] }, index=['Apr', 'May', 'Jun'])
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'