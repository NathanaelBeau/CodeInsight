string = "This is a $test$ string. Another $example$ here."
expected_output = ["test", "example"]
assert test(string) == expected_output, 'Test failed'