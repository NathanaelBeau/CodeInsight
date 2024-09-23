df0 = pd.DataFrame({'X': [6, 7, 8], 'Y': [9, 10, 11]})
column_name0 = 'X'
threshold0 = 6
expected_result =  2
result = test(df0, column_name0, threshold0)
assert result == expected_result, 'Test failed'