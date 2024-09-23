df0 = pd.DataFrame({'X': [7, 8, 9, 7, 9, 7], 'Y': [10, 11, 11, 12, 12, 12]})
col_name0 = 'X'
value0 = 7
expected_result =  3
result = test(df0, col_name0, value0)
assert result == expected_result, 'Test failed'