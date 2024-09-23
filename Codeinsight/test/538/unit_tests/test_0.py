arr0 = np.array([np.nan, 3, 2, 4])
expected_output = np.array([4., 3., 2., np.nan])
assert np.allclose(test(arr0), expected_output, equal_nan=True), 'Test failed'