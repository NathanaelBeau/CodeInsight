array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
expected_output = np.array([4, 10, 18])
assert (test(array1, array2) == expected_output).all(), 'Test failed'