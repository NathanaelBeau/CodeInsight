arr2 = np.array([[9, 10], [11, 12]])
arr3 = np.array([13, 14])
expected_result =  np.array([[9, 10, 13], [11, 12, 14]])
result = test(arr2, arr3)
assert np.array_equal(result, expected_result), 'Test failed'