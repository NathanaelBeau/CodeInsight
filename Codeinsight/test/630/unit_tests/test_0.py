arr0 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr1 = np.array([3, 1, 2])
expected_result =  np.array([[4, 5, 6], [7, 8, 9], [1, 2, 3]])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'