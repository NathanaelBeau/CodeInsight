var0 = range(1, 5)
var1 = range(7, 11)
expected_output = {1: 7, 2: 8, 3: 9, 4: 10}
assert test(var0, var1) == expected_output, 'Test failed'