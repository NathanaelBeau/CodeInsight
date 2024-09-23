# Test 1
var0 = "apple123banana456"
var1 = r'\d+'
expected_result =  ["321", "654"]
assert test(var0, var1) == expected_result, 'Test failed'