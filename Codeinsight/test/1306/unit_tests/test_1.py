arr0 = np.array([0.5, 1.0, 1.5, 2.0])
var0 = 1.5
expected_result =  (np.array([2]),)
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'