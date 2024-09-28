# Test 1
var0 = "This is a string with \\\\ double backslashes."
expected_result =  "This is a string with \\ double backslashes."
assert test(var0) == expected_result, 'Test failed'