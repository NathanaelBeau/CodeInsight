var0 = "apple,banana, orange"
var1 = " "
expected_result =  "apple,banana,"
result = test(var0, var1)
assert result == expected_result, 'Test failed'