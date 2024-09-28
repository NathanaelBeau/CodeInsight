arr2 = np.array([[[0], [1], [2]]])
var2 = 2
expected_result =  np.array([[0, 1, 2]])
result = test(arr2, var2)
assert np.array_equal(result, expected_result), 'Test failed'