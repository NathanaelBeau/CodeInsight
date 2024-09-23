str0 = 'x+13.5*10x-4e1'
var0 = r'(\d+|\W+)'
expected_output = ['x', '+', '13', '.', '5', '*', '10', 'x', '-', '4', 'e', '1']
assert test(str0, var0) == expected_output, 'Test failed'