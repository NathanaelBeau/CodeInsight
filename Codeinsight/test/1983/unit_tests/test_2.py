# Test 3
df0_3 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [None, None, None, None]})
col_name_3 = 'B'
expected_result_3 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [0, 0, 0, 0]})
result_3 = test(df0_3, col_name_3)
assert result_3.equals(expected_result_3), 'Test failed'