# Test 3
df0 = pd.DataFrame({'name': ['John', 'Jane', 'John'], 'gender': ['M', 'F', 'M']})
col_name, condition, new_value = 'name', 'John', 'Jonathan'
expected_result =  pd.DataFrame({'name': ['Jonathan', 'Jane', 'Jonathan'], 'gender': ['M', 'F', 'M']})
result = test(df0, col_name, condition, new_value)
assert result.equals(expected_result), 'Test failed'