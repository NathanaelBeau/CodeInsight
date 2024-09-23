# Test 1
df0 = pd.DataFrame({'A': ['apple', 'banana', 'cherry']})
column_name = 'A'
prefix_string = 'fruit_'
expected_result =  pd.DataFrame({'A': ['fruit_apple', 'fruit_banana', 'fruit_cherry']})
result = test(df0, column_name, prefix_string)
assert result.equals(expected_result), 'Test failed'