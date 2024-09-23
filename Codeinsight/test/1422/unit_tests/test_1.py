arr0 = np.array([[1, 2], [3, 40], [5, 60]])
var0 = 5
expected_result =  np.array([[1, 2], [3, 5], [5, 5]])
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'