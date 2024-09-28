dict0 = {'l': 'Hello', 'm': True, 'n': [1, 2, 3], 'o': {'a': 1, 'b': 2}, 'p': 5}
var0 = ('l', 'n', 'p')
expected_output = {'l': 'Hello', 'n': [1, 2, 3], 'p': 5}
assert test(dict0, var0) ==expected_output, 'Test failed'