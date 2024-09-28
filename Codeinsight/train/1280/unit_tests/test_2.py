shape0 = (2, 2)
expected_result =  np.array([[np.NaN, np.NaN], [np.NaN, np.NaN]])
result = test(shape0)
assert np.all(np.isnan(result) == np.isnan(expected_result)), 'Test failed'