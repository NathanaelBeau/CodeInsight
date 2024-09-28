lst0 = [0, 1, 2]
var0 = 3
expected_result =  np.array([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])
result = test(lst0, var0)
assert np.array_equal(result, expected_result), 'Test failed'