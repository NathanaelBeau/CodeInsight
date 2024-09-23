arr0 = np.array([5, 7, 6, 8])
expected_result =  np.array([8, 7, 6, 5])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'