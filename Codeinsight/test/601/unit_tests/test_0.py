var0_1 = 0
var1_1 = 'A'
df0_1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
expected_result_1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]}, index=['A', 1])
result_1 = test(df0_1.copy(), var0_1, var1_1)
assert result_1.equals(expected_result_1), 'Test failed'