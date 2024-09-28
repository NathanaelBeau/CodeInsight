arr0 = np.array([0, 0, 0])
arr1 = np.array([10, 20, 30])
expected_output = np.array([5, 10, 15])
assert (test(arr0, arr1)  == expected_output).all(), 'Test failed'