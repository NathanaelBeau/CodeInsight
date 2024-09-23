arr0 = np.array([1, 2])
arr1 = np.array([3, 4])
expected_result =  np.array([[1, 3], [1, 4], [2, 3], [2, 4]])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'