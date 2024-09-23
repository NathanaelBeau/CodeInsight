arr0 = np.array([[7], [8]])
col0 = np.array([[9], [10]])
expected_result =  np.array([[7, 9], [8, 10]])
result = test(arr0, col0)
assert np.array_equal(result, expected_result), 'Test failed'