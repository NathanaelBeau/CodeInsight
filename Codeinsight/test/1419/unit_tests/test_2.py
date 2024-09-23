var0_3 = 1
var1_3 = 'C'
df0_3 = pd.DataFrame({'col1': [9, 10], 'col2': [11, 12]})
expected_result_3 = pd.DataFrame({'col1': [9, 10], 'col2': [11, 12]}, index=[0, 'C'])
result_3 = test(df0_3.copy(), var0_3, var1_3)
assert result_3.equals(expected_result_3), 'Test failed'