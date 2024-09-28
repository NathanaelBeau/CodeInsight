s = "(This) is (not) a (good) (example string)."
expected_output = "This is not a good (example string)."
assert test(s) == expected_output, 'Test failed'