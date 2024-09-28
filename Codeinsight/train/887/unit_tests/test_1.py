arr0 = np.array([[10, 20], [30, 40], [50, 60]])
arr1 = np.array([2, 3, 1])
expected_result =  np.array([[50, 60], [10, 20], [30, 40]])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'