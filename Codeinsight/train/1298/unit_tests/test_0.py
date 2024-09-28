# Test 1
df0 = pd.DataFrame({'A': [3, 2, 1, 3, 2]})
column_name = 'A'
expected_result =  [1, 2, 3]
result = test(df0, column_name)
assert result == expected_result, 'Test failed'