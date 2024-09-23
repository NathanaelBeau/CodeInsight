arr0 = np.arange(20).reshape((5, 4))
var0 = [0, 1, 2, 3, 4]
var1 = [1]
expected_output = np.array([[1],
                                   [5],
                                   [9],
                                   [13],
                                   [17]])
assert (test(arr0, var0, var1)  == expected_output).all(), 'Test failed'