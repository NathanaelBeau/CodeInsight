var0 = "[INFO] User logged in"
var1 = r"^\[(\w+)\]"
expected_result =  "INFO"
assert test(var0, var1) == expected_result, 'Test failed'