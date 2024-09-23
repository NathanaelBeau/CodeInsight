dict0 = { 'a': [10, 'foo'], 'b': [5, 'bar'], 'c': [20, 'baz'], 'd': [15, 'qux'] }
var0 = 0
expected_output = ['b', 'a', 'd', 'c']
assert test(dict0, var0) ==expected_output, 'Test failed'