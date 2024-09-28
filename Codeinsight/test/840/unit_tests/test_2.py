df0 = pd.DataFrame({'M': [13.1234, 14.5678, 15.9012], 'N': [16.3456, 17.7890, 18.2345]})
column_name0 = 'M'
decimals0 = 3
expected_result =  pd.DataFrame({'M': [13.123, 14.568, 15.901], 'N': [16.3456, 17.7890, 18.2345]})
result = test(df0, column_name0, decimals0)
assert result.equals(expected_result), 'Test failed'