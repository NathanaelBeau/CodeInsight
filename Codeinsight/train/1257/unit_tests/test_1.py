# Test 2
df0_2 = pd.DataFrame({'A': [None, None, None, None], 'B': [1, 2, 3, 4]})
col_name_2 = 'A'
expected_result_2 = pd.DataFrame({'A': [0, 0, 0, 0], 'B': [1, 2, 3, 4]})
result_2 = test(df0_2, col_name_2)
assert result_2.equals(expected_result_2), 'Test failed'