arr0 = np.array([[1, 1], [2, 3], [1, 1], [5, 6]])
expected_result =  np.array([[1, 1], [2, 3], [5, 6]])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'