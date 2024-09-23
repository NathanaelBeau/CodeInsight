shape0 = (3, 3)
expected_result =  np.array([[np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan]])
result = test(shape0)
assert np.all(np.isnan(result) == np.isnan(expected_result)), 'Test failed'