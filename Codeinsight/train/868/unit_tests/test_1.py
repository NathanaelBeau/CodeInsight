arr0 = np.array([5, 15, 25, 35, 45])
var0 = 45
expected_result =  np.array([5, 15, 25, 35])
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'