str0 = "abc+def+ghi"
var0= ",+"
expected_output = "abc+def,+ghi"
assert test(str0, var0) ==expected_output, 'Test failed'