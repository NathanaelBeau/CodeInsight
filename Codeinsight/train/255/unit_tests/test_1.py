old_set_2 = np.array([10, 20, 30])
new_set_2 = np.array([5, 15, 25])
expected_output2 = np.array([7.5, 17.5, 27.5])
assert np.array_equal(test(old_set_2, new_set_2), expected_output2), 'Test failed'