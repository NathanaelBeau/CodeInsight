var0 = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20]])
var1= 3
var2= 5        
expected_output = np.array([4, 5, 9, 10, 14, 15, 19, 20])
assert (test(var0, var1, var2)  == expected_output).all(), 'Test failed'