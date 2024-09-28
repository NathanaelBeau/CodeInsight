var0 = "abc@123@def@456@ghi"
var1 = "@"
expected_result =  "abc@123@def@456"
result = test(var0, var1)
assert result == expected_result, 'Test failed'