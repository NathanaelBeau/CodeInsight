df0 = pd.DataFrame({'col1': [True, False, True], 'col2': [False, True, False]})
expected_result =  pd.DataFrame({'col1': [1, 0, 1], 'col2': [0, 1, 0]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'