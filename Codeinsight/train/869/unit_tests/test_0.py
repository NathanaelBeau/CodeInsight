shape0 = (3, 3)
var0 = True
expected_result =  np.ones((3,3), dtype=bool)
result = test(shape0, var0)
assert np.array_equal(result, expected_result), 'Test failed'