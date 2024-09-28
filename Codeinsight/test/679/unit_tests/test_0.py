shape0 = (3, 3)
var0 = 5
expected_result =  np.array([[5, 5, 5], [5, 5, 5], [5, 5, 5]])
result = test(shape0, var0)
assert np.array_equal(result, expected_result), 'Test failed'