arr0 = np.array([-10.5, 20.6, -30.7, 40.8])
expected_result =  np.array([0, 20.6, 0, 40.8])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'