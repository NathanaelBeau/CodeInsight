lst0 = [np.array([2, 3, 4,5]), np.array([5, 6, 7, 8])]
expected_output = np.array([2, 3, 4, 5, 5, 6, 7, 8])
assert (test(lst0)  == expected_output).all(), 'Test failed'