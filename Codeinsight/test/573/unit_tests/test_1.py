df0 = pd.DataFrame({'col1': [True], 'col2': [False]})
expected_result =  pd.DataFrame({'col1': [1], 'col2': [0]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'