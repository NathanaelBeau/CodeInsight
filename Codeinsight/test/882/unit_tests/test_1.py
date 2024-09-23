arr0 = np.array([[7, 8], [9, 10]])
expected_result =  np.array([[7, 8], [9, 10]])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'