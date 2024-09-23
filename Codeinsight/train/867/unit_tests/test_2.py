arr0 = np.array([1, 0])
var0 = 2
expected_result =  np.array([[0, 1], [1, 0]])
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'