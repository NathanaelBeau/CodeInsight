# Test 2
df0 = pd.DataFrame({'B': [10, 20, 30, 40, 50]})
col_name = 'B'
expected_result =  30.0
result = test(df0, col_name)
assert result == expected_result, 'Test failed'