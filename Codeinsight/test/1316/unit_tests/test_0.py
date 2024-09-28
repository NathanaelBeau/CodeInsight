# Test 1
var0 = "a,b,c(d,e),f"
expected_result =  ["a", "b", "c(d,e)", "f"]
assert test(var0) == expected_result, 'Test failed'