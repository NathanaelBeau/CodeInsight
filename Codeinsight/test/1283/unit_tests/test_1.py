str0 = "Another example\u200b\u200b\u200b with multiple \u200bzero width spaces\u200b."
expected_output = "Another example*** with multiple *zero width spaces*."
assert test(str0) ==expected_output, 'Test failed'