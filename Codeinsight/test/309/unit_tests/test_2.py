df0 = pd.DataFrame({'col1': [False, False], 'col2': [True, True]})
expected_result =  pd.DataFrame({'col1': [0, 0], 'col2': [1, 1]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'