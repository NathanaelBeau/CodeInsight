arr0 = np.array([10, 20, 30, 40, 50, 60])
var0 = 5
expected_result =  np.array([10, 20, 30, 40, 50])
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'