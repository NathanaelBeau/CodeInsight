lst0 = np.array([7, 8, 6, 5, 9])
var0 = 3
expected_result =  np.array([4, 1, 0])
result = test(lst0, var0)
assert np.array_equal(result, expected_result), 'Test failed'