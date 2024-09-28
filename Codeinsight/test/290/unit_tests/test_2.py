df0 = pd.DataFrame({'col3': ['123', '456', '789']})
col0 = 'col3'
var0 = 'pre_'
expected_output = pd.DataFrame({'col3': ['pre_123', 'pre_456', 'pre_789']})
assert test(df0, col0, var0) .equals(expected_output), 'Test failed'