df0 = pd.DataFrame({'X': [7.891, 8.234, 9.567], 'Y': [10.123, 11.456, 12.789]})
column_name0 = 'Y'
decimals0 = 1
expected_result =  pd.DataFrame({'X': [7.891, 8.234, 9.567], 'Y': [10.1, 11.5, 12.8]})
result = test(df0, column_name0, decimals0)
assert result.equals(expected_result), 'Test failed'