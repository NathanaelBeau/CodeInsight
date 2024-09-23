arr0 = np.array([7, 7, 7, 8, 8])
var0 = 7
var1 = 0
expected_result =  np.array([0, 0, 0, 8, 8])
result = test(arr0, var0, var1)
assert np.array_equal(result, expected_result), 'Test failed'