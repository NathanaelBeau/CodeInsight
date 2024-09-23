lst0 = [1, 0, 0, 0, 0]
expected_output = np.corrcoef(lst0)
assert np.array_equal(test(lst0), expected_output), 'Test failed'