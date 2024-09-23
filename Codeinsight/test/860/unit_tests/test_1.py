lst0 = np.array([])
var0 = 5
expected_result =  np.array([5])
result = test(lst0, var0)
assert np.array_equal(result, expected_result), 'Test failed'