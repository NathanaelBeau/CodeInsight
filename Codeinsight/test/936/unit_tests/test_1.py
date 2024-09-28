var0 = r'(\d+(\.\d+)?)'
var1 = 'Hello 3434.35353 World'
expected_output = '3434.35353'
assert test(var0, var1) == expected_output, 'Test failed'