lst0 = np.array([10, 20, 30, 40, 50, 60])
var0 = 2
expected_result =  np.array([5, 4])
result = test(lst0, var0)
assert np.array_equal(result, expected_result), 'Test failed'