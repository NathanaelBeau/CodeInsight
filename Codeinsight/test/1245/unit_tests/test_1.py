arr0 = np.array([10, 20, 30])
arr1 = np.array([0, 10, 20])
expected_result =  np.array([5., 15., 25.])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'