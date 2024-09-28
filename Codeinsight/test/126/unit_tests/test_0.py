lst0 = [np.array([1, 2, 3]), np.array([4, 5, 6]), np.array([7, 8, 9])]
expected_output = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
assert (test(lst0)  == expected_output).all(), 'Test failed'