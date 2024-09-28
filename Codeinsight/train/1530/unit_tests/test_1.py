# Test 2
df0 = pd.DataFrame({'fruit': ['apple', 'banana'], 'count': [10, 20]})
old_col_name, new_col_name = 'count', 'quantity'
expected_result =  pd.DataFrame({'fruit': ['apple', 'banana'], 'quantity': [10, 20]})
result = test(df0, old_col_name, new_col_name)
assert result.equals(expected_result), 'Test failed'