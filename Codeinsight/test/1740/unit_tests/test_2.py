arr2 = np.array([(11.0,), (12.0,)], dtype=[('c', np.float64)])
expected_result =  np.array([[11.0], [12.0]])
result = test(arr2)
assert np.array_equal(result, expected_result), 'Test failed'