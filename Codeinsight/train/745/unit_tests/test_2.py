var0 = 1
var1 = "abc"
var2 = "XYZ"
var3 = "abcdefgh"
expected_result =  "XYZdefgh"
result = test(var0, var1, var2, var3)
assert result == expected_result, 'Test failed'