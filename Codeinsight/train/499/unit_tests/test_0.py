arr0 = np.array([[34, 2], [0, -5], [3, 6]])
var0 = 1
expected_result =  np.array([[0, -5], [34, 2], [3, 6]])
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'