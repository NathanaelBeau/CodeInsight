df0 = pd.DataFrame({ 'X': [None, None, None, None], 'Y': [1, 2, 3, 4], 'Z': [1, 2, 3, 4] })
expected_result =  pd.Series({'X': 4, 'Y': 0, 'Z': 0})
result = test(df0)
assert result.equals(expected_result), 'Test failed'