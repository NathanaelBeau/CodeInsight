matrix0 = np.array([[7, 8], [9, 10], [11, 12]])
expected_result =  np.array([np.sqrt(113), np.sqrt(181), np.sqrt(265)])
result = test(matrix0)
assert np.array_equal(result, expected_result), 'Test failed'