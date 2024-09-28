df2 = pd.DataFrame({'C': [True, False, True, True, False, False]})
col2 = 'C'
expected_result =  pd.DataFrame({'C': [True, False, True, True, False, False], 'compared': [False, False, False, True, False, True]})
result = test(df2, col2)
assert result.equals(expected_result), 'Test failed'