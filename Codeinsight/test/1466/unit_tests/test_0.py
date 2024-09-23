# Test 1
df0 = pd.DataFrame({'A': ['apple', 'banana', 'apple'], 'B': [1, 2, 3]})
column_name = 'A'
key_value = 'apple'
expected_result =  pd.DataFrame({'A': ['apple', 'apple'], 'B': [1, 3]})
result = test(df0, column_name, key_value).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'