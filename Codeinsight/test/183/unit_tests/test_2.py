arr2 = np.array([[11, 12]])
var0 = 0
var1 = 0
expected_result =  np.array([[11, 12]])
result = test(arr2, var0, var1)
assert np.array_equal(result, expected_result), 'Test failed'