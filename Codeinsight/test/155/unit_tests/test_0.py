df0 = pd.DataFrame({ 'A': [0, 1, 0], 'B': [1, 0, 0] })
expected_result =  np.mean([(0, 1), (1, 0)])
result = test(df0)
assert np.isclose(result, expected_result), 'Test failed'