# Test 1
df0 = pd.DataFrame({'A': [1, 2, 2, 3, 3, 3]})
column_name = 'A'
expected_result =  3
result = test(df0, column_name)
assert result == expected_result, 'Test failed'