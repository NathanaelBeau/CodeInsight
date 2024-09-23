arr0 = np.array([0.12345, 0.67890, 9.87654])
var0 = 2
expected_output = ['0.12', '0.68', '9.88']
assert (test(arr0, var0)  ==  expected_output).all(), 'Test failed'