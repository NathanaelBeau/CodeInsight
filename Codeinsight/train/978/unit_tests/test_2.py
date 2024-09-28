# Test 3
df0 = pd.DataFrame({'M': [10, 20, 30, 40], 'N': ['red', 'green', 'red', 'blue']})
column_name = 'N'
key_value = 'red'
expected_result =  pd.DataFrame({'M': [10, 30], 'N': ['red', 'red']})
result = test(df0, column_name, key_value).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'