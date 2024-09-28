arr0 = np.array([[5]])
var0 = 2
expected_result =  np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 5, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
result = test(arr0, var0)
assert (result  ==  expected_result).all(), 'Test failed'