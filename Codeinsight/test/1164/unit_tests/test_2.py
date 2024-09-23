arr0 = np.array([2, 2])
arr1 = np.array([3, 3])
expected_output = np.array([2.5, 2.5])
assert (test(arr0, arr1)  == expected_output).all(), 'Test failed'