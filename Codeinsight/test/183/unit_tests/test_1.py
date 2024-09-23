arr1 = np.array([[5, 6], [7, 8], [9, 10]])
var0 = 2
var1 = 1
expected_result =  np.array([[5, 6, 0], [7, 8, 0], [9, 10, 0], [0, 0, 0], [0, 0, 0]])
result = test(arr1, var0, var1)
assert np.array_equal(result, expected_result), 'Test failed'