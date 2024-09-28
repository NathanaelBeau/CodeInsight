arr0 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
expected_result =  np.array([[1, 2], [4, 5]])
assert np.array_equal(test(arr0), expected_result), 'Test failed'