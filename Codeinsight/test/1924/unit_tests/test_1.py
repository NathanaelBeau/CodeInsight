arr1 = np.array([np.nan, np.nan, np.nan])
expected_result1 = np.array([0.0, 0.0, 0.0])
result1 = test(arr1)
assert np.array_equal(result1, expected_result1), 'Test failed'