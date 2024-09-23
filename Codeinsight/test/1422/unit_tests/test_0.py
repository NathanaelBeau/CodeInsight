arr0 = np.array([[1, 10], [15, 5], [20, 30]])
var0 = 10
expected_result =  np.array([[1, 10], [10, 5], [10, 10]])
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'