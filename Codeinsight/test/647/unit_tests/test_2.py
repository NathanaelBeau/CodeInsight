arr2 = np.array([[7, 8], [9, 10]])
var0, var1 = 0, 2
expected_result =  np.array([[7, 8, 0, 0], [9, 10, 0, 0]])
result = test(arr2, var0, var1)
assert np.array_equal(result, expected_result), 'Test failed'