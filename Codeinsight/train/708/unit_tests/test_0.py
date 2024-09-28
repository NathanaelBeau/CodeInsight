arr0 = np.array([1, 2, 3])
arr1 = np.array([1, 2, 4])
expected_result =  np.array([True, True, False])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'