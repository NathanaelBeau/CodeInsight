var0 = 1
var1 = "abc"
var2 = "XYZ"
var3 = "abcefgh"
expected_result =  "XYZefgh"
result = test(var0, var1, var2, var3)
assert result == expected_result, 'Test failed'