arr0 = np.array([1, 2, 3])
expected_output = np.vstack([arr0, arr0])
assert np.array_equal(test(arr0), expected_output), 'Test failed'