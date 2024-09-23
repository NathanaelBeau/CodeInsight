array1 = np.array([7, 8, 9])
array2 = np.array([10, 11, 12])
expected_output = np.array([70, 88, 108])
assert (test(array1, array2) == expected_output).all(), 'Test failed'