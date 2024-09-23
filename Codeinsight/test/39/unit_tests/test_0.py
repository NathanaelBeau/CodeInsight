arr0 = np.array([1.234567, 2.345678, 3.456789])
var0 = "{:.2f}"
expected_output = ['1.23', '2.35', '3.46']
assert test(arr0, var0) == expected_output, 'Test failed'