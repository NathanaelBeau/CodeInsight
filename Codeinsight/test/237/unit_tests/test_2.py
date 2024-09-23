var0 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
var1 = np.array([[0, 0, 0], [10, 10, 10], [11, 11, 11]])
expected_result =  np.array([0, 0, 0])
assert (test(var0, var1) ==  expected_result).all(), 'Test failed'