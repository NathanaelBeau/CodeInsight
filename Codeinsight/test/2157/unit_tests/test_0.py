lst0 = [1, 2, 3, 4, 5]
expected_output = np.corrcoef(lst0)
assert np.array_equal(test(lst0), expected_output), 'Test failed'