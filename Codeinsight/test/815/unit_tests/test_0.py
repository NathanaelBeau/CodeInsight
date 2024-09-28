var0 = "HELLO hello HeLLo"
var1 = "hello"
var2 = "world"
expected_result =  "world world world"
result = test(var0, var1, var2)
assert result == expected_result, 'Test failed'