str0 = "This is a test\u200b string with \u200bunicode characters\u200b."
expected_output = "This is a test* string with *unicode characters*."
assert test(str0) ==expected_output, 'Test failed'