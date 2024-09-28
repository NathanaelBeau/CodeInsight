# Test 1
var0 = "Hello, World!"
exceptions = ",!"
replacement = "_"
expected_result =  "Hello,_World!"
assert test(var0, exceptions, replacement) == expected_result, 'Test failed'