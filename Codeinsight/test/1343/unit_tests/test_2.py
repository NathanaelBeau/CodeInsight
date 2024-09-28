shape0 = (2, 2)
var0 = False
expected_result =  np.zeros((2,2), dtype=bool)
result = test(shape0, var0)
assert np.array_equal(result, expected_result), 'Test failed'