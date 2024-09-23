arr0 = np.array([1, -np.inf, 3, 4, -np.inf])
expected_result =  np.array([1, 0, 3, 4, 0])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'