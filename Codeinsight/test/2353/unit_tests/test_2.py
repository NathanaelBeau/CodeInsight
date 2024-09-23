df0 = pd.DataFrame({ 'A': [-1, -2, 3], 'B': [-4, -5, -6], 'C': [0, 0, 0] })
expected_result =  pd.DataFrame({ 'B': [-4, -5, -6], 'C': [0, 0, 0] })
result = test(df0)
assert result.equals(expected_result), 'Test failed'