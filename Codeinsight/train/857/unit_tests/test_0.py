df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
expected_result =  pd.DataFrame({'A': [-1.22474487, 0, 1.22474487], 'B': [-1.22474487, 0, 1.22474487]})
assert np.allclose(test(df0).values, expected_result.values, atol=1e-5), 'Test failed'