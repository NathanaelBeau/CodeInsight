shape0 = (3, 2, 2)
expected_result =  np.array([[[0, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]])
result = test(shape0)
assert np.array_equal(result, expected_result), 'Test failed'