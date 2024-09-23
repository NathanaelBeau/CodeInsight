df0 = pd.DataFrame({ 'variable': ['A', 'A', 'B', 'B'], 'value': [1, 2, 3, 4] })
expected_result =  pd.DataFrame({ 'A': [1, 2], 'B': [3, 4] })
result = test(df0, 'variable', 'value')
assert result.equals(expected_result), 'Test failed'