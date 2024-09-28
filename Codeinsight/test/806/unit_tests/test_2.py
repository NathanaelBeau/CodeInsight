str0 = "a+b+c+d+e"
var0= ",+"
expected_output = "a+b+c+d,+e"
assert test(str0, var0) ==expected_output, 'Test failed'