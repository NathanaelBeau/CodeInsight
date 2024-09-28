# Test 1
df0 = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
col_name = 'A'
expected_result =  3.0
result = test(df0, col_name)
assert result == expected_result, 'Test failed'