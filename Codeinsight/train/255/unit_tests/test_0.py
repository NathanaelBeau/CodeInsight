old_set_1 = np.array([1, 2, 3])
new_set_1 = np.array([4, 5, 6])
expected_output1 = np.array([2.5, 3.5, 4.5])
assert np.array_equal(test(old_set_1, new_set_1), expected_output1), 'Test failed'