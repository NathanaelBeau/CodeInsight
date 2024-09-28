dict0 = {'a': 1, 'b': None, 'c': 3, 'd': None}
var0 = 'updated'
expected_output = {'b': 'updated', 'd': 'updated'}
assert test(dict0, var0) ==expected_output, 'Test failed'