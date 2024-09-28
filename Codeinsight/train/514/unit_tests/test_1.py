var0_2 = 1
var1_2 = 'B'
df0_2 = pd.DataFrame({'col1': [5, 6], 'col2': [7, 8]})
expected_result_2 = pd.DataFrame({'col1': [5, 6], 'col2': [7, 8]}, index=[0, 'B'])
result_2 = test(df0_2.copy(), var0_2, var1_2)
assert result_2.equals(expected_result_2), 'Test failed'