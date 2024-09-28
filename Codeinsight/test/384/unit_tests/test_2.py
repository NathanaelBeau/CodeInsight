arr0 = np.array([-0.5, 0, 0.5, 1])
expected_result =  np.array([0, 0, 0.5, 1])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'