lst0 = [0, 0, 0, 0, 0]
expected_output = np.cov(lst0)
assert np.array_equal(test(lst0), expected_output), 'Test failed'