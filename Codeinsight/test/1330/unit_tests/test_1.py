df0 = pd.DataFrame({'B': ['4', '5', '6']})
column_name0 = 'B'
expected_result =  pd.DataFrame({'B': [4, 5, 6]})
result = test(df0, column_name0)
assert result.equals(expected_result), 'Test failed'