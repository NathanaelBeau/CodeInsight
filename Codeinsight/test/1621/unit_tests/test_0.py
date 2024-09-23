df0 = pd.DataFrame({ 'A': [1, 2, None, 4], 'B': [None, 2, 3, 4], 'C': [1, None, None, 4] })
expected_result =  pd.Series({'A': 1, 'B': 1, 'C': 2})
result = test(df0)
assert result.equals(expected_result), 'Test failed'