arr0 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
var0= 0
var1= 2
expected_output= np.array([[1, 3], [4, 6], [7, 9]])
assert (test(arr0, var0, var1)  == expected_output).all(), 'Test failed'