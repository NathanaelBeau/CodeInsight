var0 = "<Hello>, <world>!"
char_start = "<"
char_end = ">"
expected_result =  ["Hello", "world"]
result = test(var0, char_start, char_end)
assert result == expected_result, 'Test failed'