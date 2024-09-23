# Test 1
var0 = "Hello World!"
var1 = r"\b\w+\b"
var2 = "_"
expected_result =  "Hello_ World_!"
assert test(var0, var1, var2) == expected_result, 'Test failed'