var0 = "Hello, 世界!"
expected_result =  "Hello, \\u4e16\\u754c!"
result = test(var0)
assert result == expected_result, 'Test failed'