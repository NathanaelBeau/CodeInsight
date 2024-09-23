arr0 = np.array([[5, 6]])
var0 = 2
expected_result =  np.array([[[5, 5], [6, 6]]])
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'