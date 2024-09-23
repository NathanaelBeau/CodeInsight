df0 = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60]})
expected_result =  pd.DataFrame({'A': [-1.22474487, 0, 1.22474487], 'B': [-1.22474487, 0, 1.22474487]})
assert np.allclose(test(df0).values, expected_result.values, atol=1e-5), 'Test failed'