arr0 = np.array([5])
arr1 = np.array([6, 7])
expected_result =  np.array([[5, 6], [5, 7]])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'