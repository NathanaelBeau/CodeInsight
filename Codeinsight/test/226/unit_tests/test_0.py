df0 = pd.DataFrame({'A': ['1', '2', '3']})
column_name0 = 'A'
expected_result =  pd.DataFrame({'A': [1, 2, 3]})
result = test(df0, column_name0)
assert result.equals(expected_result), 'Test failed'