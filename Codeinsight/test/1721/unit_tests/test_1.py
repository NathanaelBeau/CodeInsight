arr0 = np.array([5, 5, 5, 6, 7, 7, 8])
expected_result =  np.array([[5, 6, 7, 8], [3, 1, 2, 1]])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'