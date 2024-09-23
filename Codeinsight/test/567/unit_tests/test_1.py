var0 = r'[aeiou]'
var1 = "Hello"
expected_result =  ["H", "ll", ""]
result = test(var0, var1)
assert result == expected_result, 'Test failed'