str0 = "   This is a test\n  With leading spaces\nAnd newlines   \n"
expected_output = "This is a test\nWith leading spaces\nAnd newlines   \n"
assert test(str0) == expected_output, 'Test failed'