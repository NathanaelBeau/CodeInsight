var0 = "Hello [world] (how) are \"you\" doing?"
expected_output = ['Hello', '[world]', '(how)', 'are', '"you"', 'doing?']
assert test(var0) == expected_output, 'Test failed'