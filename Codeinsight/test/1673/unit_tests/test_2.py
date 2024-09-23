lst0 = [np.array([1]), np.array([2, 3, 4]), np.array([5, 6, 7, 8]), np.array([9])]
expected_output = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
assert (test(lst0)  == expected_output).all(), 'Test failed'