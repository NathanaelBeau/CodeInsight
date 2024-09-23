arr0 = np.array([[9, 8, 7], [3, 2, 1], [6, 5, 4]])
expected_result =  np.array([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'