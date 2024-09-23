arr0 = np.array([10, -20, 30, -40, 50])
expected_result =  np.array([10, 0, 30, 0, 50])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'