arr0 = np.array([[[5, 6], [7, 8]], [[9, 10], [11, 12]]])
expected_result =  np.array([5, 6, 7, 8, 9, 10, 11, 12])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'