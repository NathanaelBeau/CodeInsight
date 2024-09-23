str0 = 'abcdefghijk'
var0 = r'(\d+|\W+)'
expected_output = ['abcdefghijk']
assert test(str0, var0) == expected_output, 'Test failed'