arr0 = np.array([])
arr1 = np.array([11, 12, 13])
expected_result =  np.array([11, 12, 13])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'