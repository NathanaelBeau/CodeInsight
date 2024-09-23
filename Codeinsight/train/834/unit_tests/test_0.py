df0 = pd.DataFrame({'A': [1.123, 2.567, 3.891], 'B': [4.234, 5.678, 6.912]})
column_name0 = 'A'
decimals0 = 2
expected_result =  pd.DataFrame({'A': [1.12, 2.57, 3.89], 'B': [4.234, 5.678, 6.912]})
result = test(df0, column_name0, decimals0)
assert result.equals(expected_result), 'Test failed'