arr0 = np.array([[1, 2], [3, 4]])
var0 = 1
expected_result =  np.array([[0, 0, 0, 0], [0, 1, 2, 0], [0, 3, 4, 0], [0, 0, 0, 0]])
result = test(arr0, var0)
assert (result  ==  expected_result).all(), 'Test failed'