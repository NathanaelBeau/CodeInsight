arr1 = np.array([(7.0, 8.0), (9.0, 10.0)], dtype=[('a', np.float64), ('b', np.float64)])
expected_result =  np.array([[7.0, 8.0], [9.0, 10.0]])
result = test(arr1)
assert np.array_equal(result, expected_result), 'Test failed'