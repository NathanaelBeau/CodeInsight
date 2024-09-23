var0 = 'old'
var1 = 'status'
var2 = 'new'
df0 = pd.DataFrame({'status': ['old', 'old', 'old'], 'value': [5, 6, 7]})
expected_result =  pd.DataFrame({'status': ['new', 'new', 'new'], 'value': [5, 6, 7]})
result = test(df0, var0, var1, var2)
assert result.equals(expected_result), 'Test failed'