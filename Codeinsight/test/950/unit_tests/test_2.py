arr0 = np.array([10, 20, 30, 40, 50])
var0 = 25
expected_result =  (np.array([2, 3, 4]),)
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'