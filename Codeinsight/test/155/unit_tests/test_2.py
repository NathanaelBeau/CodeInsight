df0 = pd.DataFrame({ 'M': [0, 4, 5], 'N': [6, 0, 7] })
expected_result =  np.mean([(1, 0), (2, 0), (0, 1), (2, 1)])
result = test(df0)
assert np.isclose(result, expected_result), 'Test failed'