arr0 = np.array([1, 2, 3])
arr1 = np.array([4, 5, 6])
expected_output = np.array([1, 2, 3, 4, 5, 6])
assert (test(arr0, arr1)  == expected_output).all(), 'Test failed'