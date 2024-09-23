# Test 2
df0 = pd.DataFrame({'B': ['apple', 'apple', 'banana', 'cherry', 'cherry']})
column_name = 'B'
expected_result =  3
result = test(df0, column_name)
assert result == expected_result, 'Test failed'