arr0 = np.array([])
arr1 = np.array([4, 5, 6])
expected_result =  np.array([4, 5, 6])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'