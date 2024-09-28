arr0 = np.array([45, 78, 12, 67, 89, 23])
var0 = 4
expected_result =  np.array([2, 5, 0, 3])
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'