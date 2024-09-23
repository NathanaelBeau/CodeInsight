df0 = pd.DataFrame({'A': [1.235, 2.456, 3.678]})
column_name0 = 'A'
decimals0 = 2
expected_result =  pd.DataFrame({'A': [1.24, 2.46, 3.68]})
result = test(df0, column_name0, decimals0)
assert result.equals(expected_result), 'Test failed'