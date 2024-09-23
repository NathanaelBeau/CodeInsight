arr0 = np.array([9, 10, 10, 11, 11, 11])
expected_result =  np.array([[9, 10, 11], [1, 2, 3]])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'