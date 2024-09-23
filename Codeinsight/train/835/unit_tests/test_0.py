df0 = pd.DataFrame({'A': [1, 2, 3, 2, 2, 4], 'B': [4, 5, 6, 5, 5, 7]})
col_name0 = 'A'
value0 = 2
expected_result =  3
result = test(df0, col_name0, value0)
assert result == expected_result, 'Test failed'