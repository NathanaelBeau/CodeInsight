str0 = '12345'
var0 = r'(\d+|\W+)'
expected_output = ['12345']
assert test(str0, var0) == expected_output, 'Test failed'