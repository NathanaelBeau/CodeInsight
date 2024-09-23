# Test 1
df0 = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
col_name, condition, new_value = 'A', 3, 99
expected_result =  pd.DataFrame({'A': [1, 2, 99, 4, 5]})
result = test(df0, col_name, condition, new_value)
assert result.equals(expected_result), 'Test failed'