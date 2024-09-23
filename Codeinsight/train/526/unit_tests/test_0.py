arr0 = np.array([1, 2, 3, 4, 5])
var0= 2
expected_output = np.array([1, 2, 4, 5])
assert (test(arr0, var0)  == expected_output).all(), 'Test failed'