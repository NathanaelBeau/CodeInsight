var0 = "This is a test! string@ with# some$ special characters."
expected_result2 = "This is a test string with some special characters."
assert test(var0) == expected_result2, 'Test failed'