df0 = pd.DataFrame({'B': [5, 10, 15, 20, 25, 30]})
column_name0 = 'B'
expected_result =  (11.25, 17.5, 23.75)
result = test(df0, column_name0)
assert result == expected_result, 'Test failed'