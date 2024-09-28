arr0 = np.array([[1, 3], [5, 7], [9, 11]])
expected_result =  np.array([[1, 3], [5, 7]])
assert np.array_equal(test(arr0), expected_result), 'Test failed'