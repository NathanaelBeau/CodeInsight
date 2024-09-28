arr0 = np.array([1000.567, 2000.5980, 3000.8540])
var0 = 2
expected_output = ['1000.57', '2000.6', '3000.85']
assert (test(arr0, var0)  ==  expected_output).all(), 'Test failed'