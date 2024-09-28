# Test 1
df0 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
old_col_name, new_col_name = 'A', 'X'
expected_result =  pd.DataFrame({'X': [1, 2], 'B': [3, 4]})
result = test(df0, old_col_name, new_col_name)
assert result.equals(expected_result), 'Test failed'