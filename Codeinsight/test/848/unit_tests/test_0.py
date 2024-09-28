df0 = pd.DataFrame({ 'A': [3, 1], 'B': [1, 2] })
expected_result =  pd.DataFrame({ 'A': [1, 1], 'B': [3, 2] })
result = test(df0)
assert result.equals(expected_result), 'Test failed'