arr0 = np.array([100, 200, 300, 400, 500])
var0 = 4
expected_output = np.array([100, 200, 300, 400])
assert (test(arr0, var0)  ==  expected_output).all(), 'Test failed'