arr0 = np.array([3.2, 2.8, np.nan, 4.5])
expected_output = np.array([4.5, 3.2, 2.8, np.nan])
assert np.allclose(test(arr0), expected_output, equal_nan=True), 'Test failed'