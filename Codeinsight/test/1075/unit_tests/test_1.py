arr0 = np.array([2, 3, 4, 5, 6])
arr1 = np.array([10, 11, 12, 13, 14])
expected_result =  np.array([[2.5, 2.5], [2.5, 2.5]])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'