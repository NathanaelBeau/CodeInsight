arr0 = np.array([1, 2, 3, 4, 5])
var0 = 3
var1 = 10
expected_result =  np.array([1, 2, 10, 4, 5])
result = test(arr0, var0, var1)
assert np.array_equal(result, expected_result), 'Test failed'