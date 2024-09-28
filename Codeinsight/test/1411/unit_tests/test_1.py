arr0 = np.array([True, True, False])
arr1 = np.array([True, False, False])
expected_result =  np.array([True, False, False])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'