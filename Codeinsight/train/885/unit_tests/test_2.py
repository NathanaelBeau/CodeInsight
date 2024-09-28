var0 = "Bananas are tasty. I like bananas."
var1 = "bananas"
expected_result =  "Bananas are tasty. I like ."
result = test(var0, var1)
assert result == expected_result, 'Test failed'