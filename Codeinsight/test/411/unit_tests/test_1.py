str0 = "\u200b\u200bhello"
expected_result =  "**hello"
result = test(str0)
assert result == expected_result, 'Test failed'