# Test 3
df0 = pd.DataFrame({'name': ['John', 'Jane'], 'gender': ['M', 'F']})
old_col_name, new_col_name = 'gender', 'sex'
expected_result =  pd.DataFrame({'name': ['John', 'Jane'], 'sex': ['M', 'F']})
result = test(df0, old_col_name, new_col_name)
assert result.equals(expected_result), 'Test failed'