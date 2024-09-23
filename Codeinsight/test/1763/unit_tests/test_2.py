arr0 = np.array([[1, 2, 3], [4, 5, 6]])
var0 = 0
expected_result =  arr0
result = test(arr0, var0)
assert (result  ==  expected_result).all(), 'Test failed'