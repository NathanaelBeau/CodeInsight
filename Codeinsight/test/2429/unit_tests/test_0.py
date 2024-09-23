str0 = "hello\u200bworld"
expected_result =  "hello*world"
result = test(str0)
assert result == expected_result, 'Test failed'