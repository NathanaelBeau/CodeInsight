dt = np.dtype([('x', np.float64), ('y', np.float64), ('z', np.float64)])
arr0 = np.array([(1.0, 2.0, 3.0), (4.0, 5.0, 6.0)], dtype=dt)
expected_result =  np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'