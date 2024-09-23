# Test 2
df0 = pd.DataFrame({'B': ['apple', 'banana', 'apple', 'cherry']})
column_name = 'B'
expected_result =  ['apple', 'banana', 'cherry']
result = test(df0, column_name)
assert result == expected_result, 'Test failed'