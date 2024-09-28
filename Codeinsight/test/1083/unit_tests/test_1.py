arr1 = np.array([[10, 20], [30, 40]])
var0, var1 = 2, 1
expected_result =  np.array([[10, 20, 0], [30, 40, 0], [0, 0, 0], [0, 0, 0]])
result = test(arr1, var0, var1)
assert np.array_equal(result, expected_result), 'Test failed'