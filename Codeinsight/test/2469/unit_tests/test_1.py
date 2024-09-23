arr0 = np.array([[11, 12, 13, 14], [15, 16, 17, 18], [19, 20, 21, 22]])
var0= 1
var1= 2
expected_output= np.array([[12, 13], [16, 17], [20, 21]])
assert (test(arr0, var0, var1)  == expected_output).all(), 'Test failed'