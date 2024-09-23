arr0 = np.array([[1, 2], [3, 4]])
var0 = 1
var1 = 2
expected_result =  np.array([[1, 2, 0, 0], [3, 4, 0, 0], [0, 0, 0, 0]])
result = test(arr0, var0, var1)
assert np.array_equal(result, expected_result), 'Test failed'