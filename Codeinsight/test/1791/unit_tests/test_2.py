arr0 = np.array([1000.0, 2000.0, 3000.0])
var0 = "{:.0f}"
expected_output = ['1000', '2000', '3000']
assert (test(arr0, var0)  ==  expected_output).all(), 'Test failed'