arr1 = np.array([10, 20, 30, 40])
var1 = 0
expected_result =  np.array([20, 30, 40])
result = test(arr1, var1)
assert np.array_equal(result, expected_result), 'Test failed'