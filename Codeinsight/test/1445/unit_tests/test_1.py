df0 = pd.DataFrame({'M': [10, 11, 12], 'N': [13, 14, 15]})
column_name0 = 'M'
threshold0 = 11
expected_result =  1
result = test(df0, column_name0, threshold0)
assert result == expected_result, 'Test failed'