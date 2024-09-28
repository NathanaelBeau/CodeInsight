arr0 = np.array([1.0, np.nan, 3.0, np.nan, 5.0])
expected_output = np.array([[1], [3]])
assert np.array_equal(test(arr0), expected_output), 'Test failed'