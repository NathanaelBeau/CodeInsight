str0 = "   Leading spaces\n  More leading spaces\nAnd even more spaces   \n"
expected_output = "Leading spaces\nMore leading spaces\nAnd even more spaces   \n"
assert test(str0) == expected_output, 'Test failed'