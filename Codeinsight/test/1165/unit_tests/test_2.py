arr0 = np.array([[13, 14, 15]])
arr1 = np.array([[16, 17, 18]])
expected_result =  np.array([[13, 14, 15], [16, 17, 18]])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'