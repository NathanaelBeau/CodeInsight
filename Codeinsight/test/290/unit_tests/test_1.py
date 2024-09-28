df0 = pd.DataFrame({'col2': ['abc', 'def', 'ghi']})
col0 = 'col2'
var0 = 'prefix_'
expected_output = pd.DataFrame({'col2': ['prefix_abc', 'prefix_def', 'prefix_ghi']})
assert test(df0, col0, var0) .equals(expected_output), 'Test failed'