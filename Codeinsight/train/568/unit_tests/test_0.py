str0 = "This is line 1.\tThis is line 2.\tThis is line 3."
expected_output = [['This is line 1.', 'This is line 2.', 'This is line 3.']]
assert test(str0) == expected_output, 'Test failed'