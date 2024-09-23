df0 = pd.DataFrame({ 'A': [1, 2, 3, 4], 'B': [10, 20, 30, 40] })
expected_result =  pd.DataFrame({ 'A': [0.0, 0.3333, 0.6667, 1.0], 'B': [0.0, 0.3333, 0.6667, 1.0] })
result = test(df0)
assert result.round(4).equals(expected_result), 'Test failed'