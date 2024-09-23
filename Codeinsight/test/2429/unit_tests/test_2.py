str0 = "world\u200b"
expected_result =  "world*"
result = test(str0)
assert result == expected_result, 'Test failed'