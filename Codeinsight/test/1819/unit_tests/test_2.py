arr0 = np.array([1.2, 2.5, 3.6])
arr1 = np.array([1.2, 2.6, 3.6])
expected_result =  np.array([True, False, True])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'