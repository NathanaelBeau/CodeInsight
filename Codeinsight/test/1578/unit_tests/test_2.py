arr2 = np.array([0.2, 0.4, 0.1, 0.8, 0.5])
var2 = 2
expected_result =  np.array([0.5, 0.8])
result = test(arr2, var2)
assert np.array_equal(result, expected_result), 'Test failed'