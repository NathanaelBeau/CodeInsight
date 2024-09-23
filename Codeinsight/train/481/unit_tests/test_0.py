# Test 1
df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
col_name1 = 'A'
col_name2 = 'B'
expected_result =  {1: 4, 2: 5, 3: 6}
result = test(df0, col_name1, col_name2)
assert result == expected_result, 'Test failed'