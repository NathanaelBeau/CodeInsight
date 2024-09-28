lst0 = np.array([10, 20])
var0 = 30
expected_result =  np.array([10, 20, 30])
result = test(lst0, var0)
assert np.array_equal(result, expected_result), 'Test failed'