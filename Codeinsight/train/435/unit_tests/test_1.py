var0 = "python Python pYTHON"
var1 = "python"
var2 = "java"
expected_result =  "java java java"
result = test(var0, var1, var2)
assert result == expected_result, 'Test failed'