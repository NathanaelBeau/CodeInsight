arr0 = np.array([10])
expected_result =  np.array([0])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'