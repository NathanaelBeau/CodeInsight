# Test 2
df0 = pd.DataFrame({'fruit': ['apple', 'banana', 'apple', 'cherry']})
col_name, condition, new_value = 'fruit', 'apple', 'orange'
expected_result =  pd.DataFrame({'fruit': ['orange', 'banana', 'orange', 'cherry']})
result = test(df0, col_name, condition, new_value)
assert result.equals(expected_result), 'Test failed'