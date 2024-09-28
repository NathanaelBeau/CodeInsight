df0 = pd.DataFrame({'X': [6, 7, 8], 'Y': [9, 10, 11]})
column_name0 = 'X'
threshold0 = 6
column_name1 = 'Y'
expected_result =  (2, 21)
result = test(df0, column_name0, threshold0, column_name1)
assert result == expected_result, 'Test failed'