df0 = pd.DataFrame({ 'X': [0, 0, 0], 'Y': [0, 2, 0], 'Z': [3, 0, 0] })
expected_result =  np.mean([(2, 0)])
result = test(df0)
assert np.isclose(result, expected_result), 'Test failed'