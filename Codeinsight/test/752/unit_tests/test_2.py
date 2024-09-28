arr0 = np.array([7.0, 8.0, 9.0])
expected_output = np.array([], dtype=int).reshape(0, 1)
assert np.array_equal(test(arr0), expected_output), 'Test failed'