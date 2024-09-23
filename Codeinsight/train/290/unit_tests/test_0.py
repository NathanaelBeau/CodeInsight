arr0 = np.arange(20).reshape((5, 4))
var0 = [0, 1, 3]
var1 = [0, 2]
expected_output = np.array([[0, 2],
                                   [4, 6],
                                   [12, 14]])
assert (test(arr0, var0, var1)  == expected_output).all(), 'Test failed'