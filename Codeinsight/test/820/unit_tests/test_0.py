# Test 1
df0 = pd.DataFrame({'fruit': ['apple', 'banana', 'apple']})
column_name = 'fruit'
old_value = 'apple'
new_value = 'orange'
expected_result =  pd.DataFrame({'fruit': ['orange', 'banana', 'orange']})
result = test(df0, column_name, old_value, new_value)
assert result.equals(expected_result), 'Test failed'