# Test 3
var0 = "apple, orange, banana"
var1 = r"\b\w+\b"
var2 = "+"
expected_result =  "apple+, orange+, banana+"
assert test(var0, var1, var2) == expected_result, 'Test failed'