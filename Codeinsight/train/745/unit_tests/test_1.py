var0 = 3
var1 = "abc"
var2 = "XYZ"
var3 = "abcdefgabcabcdefgabc"
expected_result =  "abcdefgabcXYZdefgabc"
result = test(var0, var1, var2, var3)
assert result == expected_result, 'Test failed'