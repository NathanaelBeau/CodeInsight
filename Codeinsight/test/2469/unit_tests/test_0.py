arr0 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
var0= 1
var1= 2
expected_output= np.array([[2, 3], [5, 6], [8, 9]])
assert (test(arr0, var0, var1)  == expected_output).all(), 'Test failed'