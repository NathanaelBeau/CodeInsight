arr0 = [1, 2, 1.8E308, 1.8E308, 42]
var0 = 1E308
expected_output = [1, 2, 0, 0, 42]
assert test(arr0, var0) ==expected_output, 'Test failed'