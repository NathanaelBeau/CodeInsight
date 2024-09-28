arr1 = np.array([[np.nan, 2, 3], [4, np.nan, 6], [7, 8, np.nan]])
expected_result =  np.array([[5.5, 2, 3], [4, 5, 6], [7, 8, 4.5]])
result = test(arr1)
assert np.array_equal(result, expected_result), 'Test failed'