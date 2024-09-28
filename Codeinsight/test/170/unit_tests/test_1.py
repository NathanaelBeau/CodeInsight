matrix0 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
var0 = 3
expected_result =  np.array([[1,2,3],[5,6,7],[9,10,11]])
result = test(matrix0, var0)
assert np.array_equal(result, expected_result), 'Test failed'