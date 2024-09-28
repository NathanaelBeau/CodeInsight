var0 = range(1, 6)
var1 = range(5, 10)
expected_output = {1: 5, 2: 6, 3: 7, 4: 8, 5: 9}
assert test(var0, var1) == expected_output, 'Test failed'