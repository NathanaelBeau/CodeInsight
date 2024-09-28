str0 = "Hello\\nWorld"
expected_result =  "Hello\nWorld"
result = test(str0)
assert result == expected_result, 'Test failed'