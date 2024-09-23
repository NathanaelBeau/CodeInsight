arr0 = np.array([1, 2, 3])
arr1 = np.array([4, 5, 6])
expected_result =  np.array([1, 2, 3, 4, 5, 6])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'