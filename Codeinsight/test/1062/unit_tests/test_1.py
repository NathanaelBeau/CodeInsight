arr0 = np.array([np.nan, 10, 20, np.nan, 40])
expected_result =  np.array([10., 10., 20., 30., 40.])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'