arr0 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
expected_result =  np.array([12, 15, 18])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'