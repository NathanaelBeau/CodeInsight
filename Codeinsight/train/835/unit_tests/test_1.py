df0 = pd.DataFrame({'M': [13, 14, 14, 15, 16, 16], 'N': [17, 18, 18, 19, 20, 20]})
col_name0 = 'M'
value0 = 13
expected_result =  1
result = test(df0, col_name0, value0)
assert result == expected_result, 'Test failed'