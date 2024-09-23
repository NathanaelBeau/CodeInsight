arr0 = np.array([1, 2, np.nan, 3, 4, np.nan])
expected_result =  np.array([1, 2, 3, 4])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'