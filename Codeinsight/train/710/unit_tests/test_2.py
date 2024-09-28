# Test 3
df0 = pd.DataFrame({'colors': ['red', 'blue', 'yellow', 'red']})
column_name = 'colors'
old_value = 'red'
new_value = 'green'
expected_result =  pd.DataFrame({'colors': ['green', 'blue', 'yellow', 'green']})
result = test(df0, column_name, old_value, new_value)
assert result.equals(expected_result), 'Test failed'