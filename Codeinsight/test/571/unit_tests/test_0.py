lst0 = ['1', '2', '3']
var0 = 'X'
var1 = 2
expected_output = {1: ['X'], 2: ['X', 'X'], 3: ['X', 'X'], 4: ['X']}
assert test(lst0, var0, var1) ==expected_output, 'Test failed'