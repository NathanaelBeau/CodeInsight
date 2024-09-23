arr0 = np.array([1, 2, 3, 6, 7, 8])
var0 = 5
var1 = 0
expected_result =  np.array([1, 2, 3, 0, 0, 0])
result = test(arr0, var0, var1)
assert np.array_equal(result, expected_result), 'Test failed'