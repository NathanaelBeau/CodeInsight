arr0 = np.array([7, 8, 9])
arr1 = np.array([10, 11, 12])
expected_result =  np.array([7, 8, 9, 10, 11, 12])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'