arr0 = np.array([[1], [2], [3]])
arr1 = np.array([[7], [8], [9]])
expected_result =  np.array([[7], [16], [27]])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'