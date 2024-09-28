str0 = "Another   example    with multiple spaces"
expected_output = ['Another', '   ', 'example', '    ', 'with', ' ', 'multiple', ' ', 'spaces']
assert test(str0) == expected_output, 'Test failed'