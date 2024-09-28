lst0 = np.array([1, 3, 2, 4, 5])
var0 = 3
expected_result =  np.array([4, 3, 1])
result = test(lst0, var0)
assert np.array_equal(result, expected_result), 'Test failed'