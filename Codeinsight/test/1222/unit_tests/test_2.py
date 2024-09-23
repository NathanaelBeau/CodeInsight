dict0 = { 'a': [1, 'foo'], 'b': [1, 'bar'], 'c': [1, 'baz'] }
var0 = 1
expected_output = ['b', 'c', 'a']
assert test(dict0, var0) ==expected_output, 'Test failed'