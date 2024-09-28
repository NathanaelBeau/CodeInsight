arr0 = np.array([10, 30, 50])
arr1 = np.array([10, 20, 30, 40, 50])
expected_result =  np.array([0, 2, 4])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'