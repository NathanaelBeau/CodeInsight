arr0 = np.array([6, 7, 8, 9, 10])
var0 = -1
expected_result =  np.array([7, 8, 9, 10, 6])
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'