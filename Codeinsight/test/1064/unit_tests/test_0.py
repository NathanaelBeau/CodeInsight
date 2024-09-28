arr0 = np.array([[1, np.nan, 3], [4, 5, np.nan], [7, 8, 9]])
expected_result =  np.array([[1, 6.5, 3], [4, 5, 6], [7, 8, 9]])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'