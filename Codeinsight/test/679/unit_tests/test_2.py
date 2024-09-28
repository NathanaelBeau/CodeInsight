shape0 = (1, 5)
var0 = 9
expected_result =  np.array([[9, 9, 9, 9, 9]])
result = test(shape0, var0)
assert np.array_equal(result, expected_result), 'Test failed'