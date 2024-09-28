arr0 = np.array([10, -10, 0, 20, -20])
expected_output = np.array([10, -10, 20, -20])
assert np.array_equal(test(arr0), expected_output), 'Test failed'