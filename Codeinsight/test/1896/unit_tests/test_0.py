var0 = "This is a [test] string with [multiple] brackets."
char_start = "["
char_end = "]"
expected_result =  ["test", "multiple"]
result = test(var0, char_start, char_end)
assert result == expected_result, 'Test failed'