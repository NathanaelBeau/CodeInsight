arr0 = np.array([[4, 5, 6], [7, 8, 9], [1, 2, 3]])
var0 = 2
expected_result =  np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'