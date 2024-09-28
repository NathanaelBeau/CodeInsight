dict0 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
var0 = 'a'
var1 = 'c'
var2 = 'e'
expected_output = {'a': 1, 'c': 3, 'e': None}
assert test(dict0, var0, var1, var2) ==expected_output, 'Test failed'