arr0 = np.array([0.12345, 0.67890, 9.87654])
var0 = "{:.1f}"
expected_output = ['0.1', '0.7', '9.9']
assert test(arr0, var0) == expected_output, 'Test failed'