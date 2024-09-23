lst1 = [1, 2, 0, 2]
var1 = 3
expected_result =  np.array([[0., 1., 0.], [0., 0., 1.], [1., 0., 0.], [0., 0., 1.]])
result = test(lst1, var1)
assert np.array_equal(result, expected_result), 'Test failed'