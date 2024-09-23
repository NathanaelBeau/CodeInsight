arr0 = np.array([1.5, 2.5, 3.5, 4.5])
var0 = 0
expected_result =  np.array([2.5, 3.5, 4.5])
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'