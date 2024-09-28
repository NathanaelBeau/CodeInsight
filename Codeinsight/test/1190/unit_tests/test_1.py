arr0 = np.array([8, 9])
arr1 = np.array([10])
expected_result =  np.array([[8, 10], [9, 10]])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'