df0 = pd.DataFrame({'C': [7.12345, 8.67891]})
column_name0 = 'C'
decimals0 = 4
expected_result =  pd.DataFrame({'C': [7.1234, 8.6789]})
result = test(df0, column_name0, decimals0)
assert result.equals(expected_result), 'Test failed'