arr0 = np.array([1, np.nan, 3, 4, np.nan, 6])
expected_result =  np.array([1., 2., 3., 4., 5., 6.])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'