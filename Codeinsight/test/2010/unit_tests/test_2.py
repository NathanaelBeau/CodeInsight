arr0 = np.array([[1, 2], [np.inf, -np.inf], [np.nan, 6]])
expected_result =  np.array([[1, 2]])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'