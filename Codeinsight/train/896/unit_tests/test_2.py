df0 = pd.DataFrame({'B': [4.8910, 5.6123, 6.7345]})
column_name0 = 'B'
decimals0 = 3
expected_result =  pd.DataFrame({'B': [4.891, 5.612, 6.734]})
result = test(df0, column_name0, decimals0)
assert result.equals(expected_result), 'Test failed'