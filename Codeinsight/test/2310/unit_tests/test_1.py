arr0 = np.array([[1, 2], [3, 4], [5, 6]])
var0 = 4
expected_result =  (np.array([1]), np.array([1]))
result = test(arr0, var0)
assert result == expected_result, 'Test failed'