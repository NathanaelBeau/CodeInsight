lst2 = [0, 0, 1]
var2 = 2
expected_result =  np.array([[1., 0.], [1., 0.], [0., 1.]])
result = test(lst2, var2)
assert np.array_equal(result, expected_result), 'Test failed'