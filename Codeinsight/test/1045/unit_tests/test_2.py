var0 = "No special characters here."
char_start = "{"
char_end = "}"
expected_result =  []
result = test(var0, char_start, char_end)
assert result == expected_result, 'Test failed'