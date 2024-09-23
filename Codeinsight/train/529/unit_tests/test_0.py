arr0 = np.array([10, 5, 4, 13, 10, 1, 1, 22, 7, 3, 15, 9])
arr1 = np.array([3, 4, 9, 10, 13, 15, 16, 18, 19, 20, 21, 22, 23])
expected_output = True
assert test(arr0, arr1) ==expected_output, 'Test failed'