array1 = np.array([0, 1, 2])
array2 = np.array([3, 4, 5])
expected_output = np.array([0, 4, 10])
assert (test(array1, array2) == expected_output).all(), 'Test failed'