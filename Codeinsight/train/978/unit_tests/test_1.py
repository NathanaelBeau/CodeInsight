# Test 2
df0 = pd.DataFrame({'X': ['cat', 'dog', 'cat', 'dog'], 'Y': [4, 5, 6, 7]})
column_name = 'X'
key_value = 'dog'
expected_result =  pd.DataFrame({'X': ['dog', 'dog'], 'Y': [5, 7]})
result = test(df0, column_name, key_value).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'