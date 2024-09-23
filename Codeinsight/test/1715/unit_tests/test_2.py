arr0 = np.array([False, False])
arr1 = np.array([False, True])
expected_result =  np.array([False, False])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'