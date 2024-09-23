arr0 = np.array([True, False, True])
arr1 = np.array([False, False, True])
expected_result =  np.array([False, False, True])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'