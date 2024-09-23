df0 = pd.DataFrame({ 'M': [1, 2, 3, 4], 'N': [1, 2, 3, 4], 'O': [1, 2, 3, 4] })
expected_result =  pd.Series({'M': 0, 'N': 0, 'O': 0})
result = test(df0)
assert result.equals(expected_result), 'Test failed'