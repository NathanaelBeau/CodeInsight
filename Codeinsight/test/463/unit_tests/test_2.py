arr0 = np.array([[7, 8], [7, 8], [7, 8]])
expected_result =  np.array([[7, 8]])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'