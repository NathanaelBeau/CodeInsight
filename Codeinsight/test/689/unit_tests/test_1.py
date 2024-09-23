df0 = pd.DataFrame({ 'variable': ['X', 'X', 'Y', 'Y'], 'value': [10, 20, 30, 40] })
expected_result =  pd.DataFrame({ 'X': [10, 20], 'Y': [30, 40] })
result = test(df0, 'variable', 'value')
assert result.equals(expected_result), 'Test failed'