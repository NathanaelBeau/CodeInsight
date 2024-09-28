arr2 = np.array([[1, 2, 3], [4, 5, 6], [np.nan, np.nan, np.nan]])
expected_result =  np.array([[1, 2, 3], [4, 5, 6], [2.5, 3.5, 4.5]])
result = test(arr2)
assert np.array_equal(result, expected_result), 'Test failed'