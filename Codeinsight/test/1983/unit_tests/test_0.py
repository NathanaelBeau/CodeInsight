# Test 1
df0_1 = pd.DataFrame({'A': [1, 2, None, 4], 'B': [None, 2, 3, 4]})
col_name_1 = 'A'
expected_result_1 = pd.DataFrame({'A': [1.0, 2.0, 0.0, 4.0], 'B': [None, 2.0, 3.0, 4.0]})
result_1 = test(df0_1, col_name_1)
assert result_1.equals(expected_result_1), 'Test failed'