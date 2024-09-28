arr0 = np.array([12, 24, 35, 24, 88, 120, 155, 88, 120, 155])
var0 = 4
expected_result =  np.array([120, 120, 155, 155])
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'