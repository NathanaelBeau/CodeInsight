dict0 = {'l': 1, 'm': 2, 'n': 3, 'o': 4, 'p': 5}
var0 = ('l', 'n')
expected_output = {'l': 1, 'n': 3}
assert test(dict0, var0) ==expected_output, 'Test failed'