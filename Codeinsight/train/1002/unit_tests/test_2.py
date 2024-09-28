var0 = "hello,,world"
expected_result =  ["hello", "0", "world"]
result = test(var0)
assert result == expected_result, 'Test failed'