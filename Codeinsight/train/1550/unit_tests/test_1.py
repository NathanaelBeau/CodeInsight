arr0 = np.array([[[9, 10], [11, 12]], [[13, 14], [15, 16]]])
expected_result =  np.array([[9, 10], [11, 12], [13, 14], [15, 16]])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'