lst0 = ['a', 'b', 'c', 'b', 'b', 'c']
var0 = 'b'
var1 = 2
expected_output = ['a', 2, 'c', 2, 2, 'c']
assert test(lst0, var0, var1) ==expected_output, 'Test failed'