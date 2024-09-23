matrix0 = np.array([[1,2,3],[4,5,6],[7,8,9]])
var0 = 2
expected_result =  np.array([[1,2],[4,5],[7,8]])
result = test(matrix0, var0)
assert np.array_equal(result, expected_result), 'Test failed'