arr0 = np.array([1.0, np.nan, 3.0, np.nan])
expected_result =  np.array([1.0, 0.0, 3.0, 0.0])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'