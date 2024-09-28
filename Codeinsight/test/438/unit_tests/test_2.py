# Test 2
var0 = "123 abc 456"
var1 = r"\d+"
var2 = "-"
expected_result =  "123- abc 456-"
assert test(var0, var1, var2) == expected_result, 'Test failed'