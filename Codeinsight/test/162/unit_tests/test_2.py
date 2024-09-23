arr2 = np.array([0, 1, 2, 3, 4, 5])
var2 = 4
expected_result =  np.array([[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]])
result = test(arr2, var2)
assert np.array_equal(result, expected_result), 'Test failed'