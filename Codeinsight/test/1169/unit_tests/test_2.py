var0 = "\\Backslashes\\Everywhere\\\\"
expected_result =  "BackslashesEverywhere"
result = test(var0)
assert result == expected_result, 'Test failed'