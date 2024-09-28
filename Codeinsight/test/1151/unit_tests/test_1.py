arr0 = np.array([13, 14, 15])
expected_result =  np.array([13, 14, 15])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'