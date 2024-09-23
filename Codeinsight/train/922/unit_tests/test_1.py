str0 = "1234567"
char0 = ':'
expected_result =  "12:34:56:7"
result = test(str0, char0)
assert result == expected_result, 'Test failed'