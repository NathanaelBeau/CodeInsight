# Test 2
df0 = pd.DataFrame({'numbers': [1, 2, 3, 1]})
column_name = 'numbers'
old_value = 1
new_value = 10
expected_result =  pd.DataFrame({'numbers': [10, 2, 3, 10]})
result = test(df0, column_name, old_value, new_value)
assert result.equals(expected_result), 'Test failed'