df0 = pd.DataFrame({'A': [10, 20, 30, 40, 50]})
column_name0 = 'A'
expected_result =  (20.0, 30.0, 40.0)
result = test(df0, column_name0)
assert result == expected_result, 'Test failed'