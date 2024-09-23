arr0 = np.array([[1,2], [3,4]])
col0 = np.array([[5], [6]])
expected_result =  np.array([[1, 2, 5], [3, 4, 6]])
result = test(arr0, col0)
assert np.array_equal(result, expected_result), 'Test failed'