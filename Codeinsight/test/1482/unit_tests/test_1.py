# Test 3
var0 = "abcDEFghiJKL"
var1 = r'[a-z]+'
expected_result =  "DEFJKL"
assert test(var0, var1) == expected_result, 'Test failed'