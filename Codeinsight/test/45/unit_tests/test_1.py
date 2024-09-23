arr0 = np.array([10, 20])
arr1 = np.array([30, 40])
expected_result =  np.array([[10, 30], [20, 40]])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'