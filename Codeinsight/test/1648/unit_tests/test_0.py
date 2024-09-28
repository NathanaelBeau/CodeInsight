arr0 = np.array([[1, 2], [3, 4]])
arr1 = np.array([[2, 0], [0, 2]])
expected_result =  np.array([[2, 0], [0, 8]])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'