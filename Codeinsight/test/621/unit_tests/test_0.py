s = "This is a (test) string with (multiple) (words) in (parentheses)."
expected_output = "This is a test string with multiple words in parentheses."
assert test(s) == expected_output, 'Test failed'