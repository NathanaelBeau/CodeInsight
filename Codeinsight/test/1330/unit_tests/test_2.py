df0 = pd.DataFrame({'C': ['7', '8', '9']})
column_name0 = 'C'
expected_result =  pd.DataFrame({'C': [7, 8, 9]})
result = test(df0, column_name0)
assert result.equals(expected_result), 'Test failed'