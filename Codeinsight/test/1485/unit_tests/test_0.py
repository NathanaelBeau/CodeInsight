arr0 = np.array([3, 1, 2])
expected_result =  np.array([0, 2, 1])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'