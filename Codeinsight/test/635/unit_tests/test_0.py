arr0 = np.array([1.0, np.nan, 2.0, np.nan, 3.0])
expected_result =  np.array([True, False, True, False, True])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'