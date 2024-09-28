arr0 = np.array([[1, 2], [3, 4]])
arr1 = np.array([[1, 2], [3, 4]])
expected_result =  np.array([[True, True], [True, True]])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'