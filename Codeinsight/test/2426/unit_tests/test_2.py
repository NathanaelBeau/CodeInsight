str0 = "123|456|789"
str1 = "|"
expected_result =  ["123|456", "789"]
result = test(str0, str1)
assert result == expected_result, 'Test failed'